from flask import Blueprint, request, jsonify
import json
import hashlib
from werkzeug.exceptions import Unauthorized

from .user import User
from src.shared.database.db import db
from src.shared.utils.jwt_handler import JWTHandler
from src.shared.utils.mail_handler import send_email
from src.shared.middlewares.auth_middleware import auth_middleware
from src.shared.middlewares.role_middleware import role_middleware

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('', methods=['GET'])
@auth_middleware
@role_middleware
def index() -> json:
    page, per_page = request.args.get('page'), 10
    users = User.query.paginate(page, per_page, error_out=False)
    return jsonify(users), 200


@user_bp.route('', methods=['POST'])
def store() -> json:
    (
        username,
        email,
        role,
        password,
        password_confirmation
    ) = request.json.values()

    if password != password_confirmation:
        raise Unauthorized('Password and confirmation do not match')

    hashed_password = hashlib.blake2b(bytes(password, 'utf-8')).hexdigest()
    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        role=role
    )
    db.session.add(new_user)
    db.session.commit()

    send_email(
        new_user.email,
        f'Welcome {new_user.username}',
        'We are glad to have you here with us, we hope you enjoy our platform'
    )

    return json.dumps({'success': f'Welcome, {new_user.username}!'}), 201


@user_bp.route('/<int:id>', methods=['PUT'])
@auth_middleware
def update(id: int) -> json:
    username = request.json['username']

    user = User.query.get_or_404(id)
    user.name = username
    db.session.commit()

    return jsonify(user), 200


@user_bp.route('/<int:id>', methods=['DELETE'])
@auth_middleware
def delete(id: int) -> json:
    user_to_delete = User.query.get_or_404(id)

    db.session.delete(user_to_delete)
    db.session.commit()
    return json.dumps({'succes': 'User deleted'}), 200


@user_bp.route('/auth', methods=['POST'])
def authenticate() -> json:
    if 'email' not in request.json or 'password' not in request.json:
        raise Unauthorized('Invalid credentials')

    email, password = request.json.values()

    user = User.query.filter_by(email=email).first()

    if not user:
        raise Unauthorized('Invalid credentials')

    if user.password != hashlib.blake2b(bytes(password, 'utf-8')).hexdigest():
        raise Unauthorized('Invalid credentials')

    jwt_handler = JWTHandler(user.id)

    return json.dumps(
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'token': jwt_handler.sign()
        }
    ), 201
