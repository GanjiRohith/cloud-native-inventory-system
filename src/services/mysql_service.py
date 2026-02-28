from src.config.db import db
from sqlalchemy import text

from src.models.user import User
from src.models.product import Product
from src.models.inventory import Inventory
from src.models.order import Order
from src.models.order_item import OrderItem

from src.config.mongo import mongo_db


# ================= USER =================

def register_user_mysql(data):

    existing = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing:
        return {"error": "User exists"}

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "MYSQL REGISTERED"}


def login_mysql(data):

    user = User.query.filter_by(
        email=data["email"],
        password=data["password"]
    ).first()

    if not user:
        return {"error": "Invalid login"}

    return {
        "id": user.id,
        "role": user.role
    }


# ================= PRODUCT =================

def create_product_mysql(data):

    product = Product(
        name=data["name"],
        price=data["price"]
    )

    db.session.add(product)
    db.session.commit()

    inventory = Inventory(
        product_id=product.id,
        quantity=int(data.get("quantity", 0))
    )

    db.session.add(inventory)
    db.session.commit()

    return {"message": "Product + Inventory Added"}


def get_products_mysql():

    query = text("""
        SELECT p.id,
               p.name,
               p.price,
               i.quantity
        FROM products p
        JOIN inventory i
        ON p.id = i.product_id
    """)

    result = db.session.execute(query)

    return [dict(row._mapping) for row in result]


# ================= ORDER =================

def create_order_mysql(data):

    try:

        order = Order(user_id=int(data["user_id"]))
        db.session.add(order)
        db.session.flush()

        for item in data["products"]:

            pid = int(item["product_id"])
            qty = int(item["quantity"])

            inventory = Inventory.query.filter_by(
                product_id=pid
            ).first()

            if not inventory:
                return {"error": "Inventory missing"}

            if inventory.quantity < qty:
                return {"error": "Out of stock"}

            inventory.quantity -= qty

            order_item = OrderItem(
                order_id=order.id,
                product_id=pid,
                quantity=qty
            )

            db.session.add(order_item)

        db.session.commit()

        mongo_db.logs.insert_one({
            "event": "MYSQL_ORDER",
            "order_id": order.id
        })

        return {"message": "MYSQL ORDER CREATED"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def get_orders_mysql():

    query = text("""
        SELECT o.id,
               o.user_id,
               oi.product_id,
               oi.quantity
        FROM orders o
        JOIN order_items oi
        ON o.id = oi.order_id
    """)

    result = db.session.execute(query)

    return [dict(row._mapping) for row in result]