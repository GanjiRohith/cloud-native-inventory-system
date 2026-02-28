from flask import Blueprint, request, jsonify

from src.services.db_selector import (
    register_service,
    login_service,
    create_user_service
)

user_bp = Blueprint("user", __name__)


# ---------- CREATE USER ----------
@user_bp.route("/users", methods=["POST"])
def create_user():

    data = request.json
    return jsonify(create_user_service(data))


# ---------- REGISTER ----------
@user_bp.route("/register", methods=["POST"])
def register():

    try:
        data = request.json
        print("REGISTER DATA:", data)

        result = register_service(data)

        return jsonify(result)

    except Exception as e:
        print("REGISTER ERROR:", e)
        return jsonify({"error": str(e)})

# ---------- LOGIN ----------
@user_bp.route("/login", methods=["POST"])
def login():

    data = request.json
    return jsonify(login_service(data))