from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models import Item
from ..schemas import ItemSchema


inv_bp = Blueprint('inventory', __name__)
item_schema = ItemSchema()


@inv_bp.route('/', methods=['GET'])
@jwt_required()
def get_items():
    items = Item.query.all()
    return item_schema.dump(items, many=True)


@inv_bp.route('/', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    item = Item(name=data['name'], quantity=data['quantity'])
    db.session.add(item)
    db.session.commit()
    return item_schema.dump(item), 201