
from flask import Blueprint, request, jsonify
from src.services.db_selector import create_order_service
from src.services.mysql_service import get_orders_mysql

order_bp = Blueprint("order", __name__)


@order_bp.route("/orders", methods=["POST"])
def create_order():

    data = request.json
    result = create_order_service(data)

    return jsonify(result)


from flask import Blueprint, request, jsonify
from src.services.db_selector import create_order_service
from src.services.mysql_service import get_orders_mysql

order_bp = Blueprint("order", __name__)


# -------- CREATE ORDER --------
@order_bp.route("/orders", methods=["POST"])
def create_order():

    data = request.json
    result = create_order_service(data)

    return jsonify(result)


# -------- GET ORDERS --------
@order_bp.route("/orders", methods=["GET"])
def get_orders():

    return jsonify(get_orders_mysql())