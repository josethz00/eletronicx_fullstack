from flask import Blueprint, request, jsonify
import json

from src.modules.items.item import Item
from src.shared.database.db import db
from src.shared.middlewares.auth_middleware import auth_middleware
from src.shared.middlewares.role_middleware import role_middleware
from src.shared.utils.image_upload_handler import ImageUploadHandler

item_bp = Blueprint('items', __name__, url_prefix='/items')


@item_bp.route('', methods=['GET'])
@auth_middleware
def index() -> json:
    page, per_page = int(request.args.get('page')), 10
    items = Item.query.paginate(page, per_page, error_out=False)
    return jsonify(items.items), 200


@item_bp.route('', methods=['POST'])
@auth_middleware
@role_middleware
def store() -> json:
    name, price, quantity, category_id = request.form.values()

    if 'item_file' not in request.files:
        new_item = Item(
            name=name,
            price=price,
            quantity=quantity,
            category_id=category_id
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item), 201

    file_data = request.files['item_file']
    upload_handler = ImageUploadHandler()

    if file_data:
        try:
            image_url = upload_handler.uploadFile(file_data)
            new_item = Item(
                name=name,
                price=price,
                image_url=image_url,
                quantity=quantity,
                category_id=category_id
            )
            db.session.add(new_item)
            db.session.commit()
            return jsonify(new_item), 201
        except Exception:
            db.session.rollback()
            raise


@item_bp.route('/<int:id>', methods=['PUT'])
@auth_middleware
@role_middleware
def update(id: int) -> json:
    name, price, quantity = request.json.values()

    item = Item.query.get_or_404(id)
    item.name, item.price, item.quantity = name, price, quantity
    db.session.commit()

    return jsonify(item), 200


@item_bp.route('/<int:id>', methods=['DELETE'])
@auth_middleware
@role_middleware
def delete(id: int) -> json:
    item_to_delete = Item.query.get_or_404(id)

    db.session.delete(item_to_delete)
    db.session.commit()
    return json.dumps({'succes': 'Item deleted'}), 200
