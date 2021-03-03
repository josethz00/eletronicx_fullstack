from flask import Blueprint, request, jsonify
import json

from src.modules.categories.category import Category
from src.shared.database.db import db
from src.shared.middlewares.auth_middleware import auth_middleware
from src.shared.middlewares.role_middleware import role_middleware

category_bp = Blueprint('category', __name__, url_prefix='/categories')


@category_bp.route('', methods=['GET'])
@auth_middleware
def index() -> json:
    page, per_page = request.args.get('page'), 10
    categories = Category.query.paginate(page, per_page, error_out=False)
    return jsonify(categories), 200


@category_bp.route('', methods=['POST'])
@auth_middleware
@role_middleware
def store() -> json:
    name = request.json['name']

    new_category = Category(
        name=name
    )
    db.session.add(new_category)
    db.session.commit()

    return json.dumps(
        {
            'success': f'New category created: {new_category.name}!'
        }
    ), 201


@category_bp.route('/<int:id>', methods=['PUT'])
@auth_middleware
@role_middleware
def update(id: int) -> json:
    new_name = request.json['name']

    category = Category.query.get_or_404(id)
    category.name = new_name
    db.session.commit()

    return jsonify(category), 200


@category_bp.route('/<int:id>', methods=['DELETE'])
@auth_middleware
@role_middleware
def delete(id: int) -> json:
    category_to_delete = Category.query.get_or_404(id)

    db.session.delete(category_to_delete)
    db.session.commit()
    return json.dumps({'success': 'Category deleted'}), 200
