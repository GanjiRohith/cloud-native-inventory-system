from bson.objectid import ObjectId
from src.config.mongo import mongo_db


# ================= USER =================

def create_user_mongo(data):

    mongo_db.users.insert_one({
        "name": data["name"],
        "email": data["email"]
    })

    return {"message": "Mongo user created"}


def register_user_mongo(data):

    existing = mongo_db.users.find_one(
        {"email": data["email"]}
    )

    if existing:
        return {"error": "User exists"}

    mongo_db.users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
        "role": data["role"]
    })

    return {"message": "Mongo Registered"}


def login_mongo(data):

    user = mongo_db.users.find_one({
        "email": data["email"],
        "password": data["password"]
    })

    if not user:
        return {"error": "Invalid login"}

    return {
        "id": str(user["_id"]),
        "role": user["role"]
    }


# ================= PRODUCT =================

def create_product_mongo(data):

    mongo_db.products.insert_one({
        "name": data["name"],
        "price": data["price"],
        "quantity": int(data.get("quantity", 0))
    })

    return {"message": "Mongo Product Added"}


def get_products_mongo():

    products = mongo_db.products.find()

    result = []

    for p in products:
        result.append({
            "id": str(p["_id"]),
            "name": p["name"],
            "price": p["price"],
            "quantity": p.get("quantity", 0)
        })

    return result


# ================= ORDER =================

def create_order_mongo(data):

    try:

        items = []

        for item in data["products"]:

            pid = str(item["product_id"])

            product = mongo_db.products.find_one(
                {"_id": ObjectId(pid)}
            )

            if not product:
                return {"error": "Product not found"}

            qty = int(item["quantity"])

            if product["quantity"] < qty:
                return {"error": "Out of stock"}

            mongo_db.products.update_one(
                {"_id": ObjectId(pid)},
                {"$inc": {"quantity": -qty}}
            )

            items.append({
                "product_id": pid,
                "quantity": qty
            })

        order = {
            "user_id": data["user_id"],
            "items": items
        }

        result = mongo_db.orders.insert_one(order)

        mongo_db.logs.insert_one({
            "event": "MONGO_ORDER",
            "order_id": str(result.inserted_id)
        })

        return {"message": "Mongo Order Created"}

    except Exception as e:
        return {"error": str(e)}


def get_orders_mongo():

    orders = mongo_db.orders.find()

    result = []

    for o in orders:
        for item in o["items"]:
            result.append({
                "id": str(o["_id"]),
                "user_id": o["user_id"],
                "product_id": item["product_id"],
                "quantity": item["quantity"]
            })

    return result