from flask import Blueprint, request, jsonify
from src.services.db_selector import create_product_service , get_products_service


product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["POST"])
def create_product():

    data = request.json
    result = create_product_service(data)

    return jsonify(result)

@product_bp.route("/products", methods=["GET"])
def get_products():

    db = request.args.get("db")

    from src.services.db_selector import get_products_service

    return jsonify(get_products_service(db))