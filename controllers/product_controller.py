from flask import Blueprint, jsonify, request
from models.product import Product, products

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    return jsonify([product.__dict__ for product in products])

@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((product for product in products if product.id == id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.__dict__)

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_id = max(product.id for product in products) + 1
    new_product = Product(new_id, data['name'], data['price'])
    products.append(new_product)
    return jsonify(new_product.__dict__), 201
