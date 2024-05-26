from flask import Blueprint, jsonify, request
from models.order import Order, orders

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([order.__dict__ for order in orders])

@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order.__dict__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_id = max(order.id for order in orders) + 1
    new_order = Order(new_id, data['product_id'], data['quantity'])
    orders.append(new_order)
    return jsonify(new_order.__dict__), 201
