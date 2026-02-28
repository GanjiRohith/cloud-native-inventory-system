# ================= MYSQL =================
from src.services.mysql_service import (
    register_user_mysql,
    login_mysql,
    create_product_mysql,
    get_products_mysql,
    create_order_mysql,
    get_orders_mysql
)

# ================= MONGO =================
from src.services.mongo_service import (
    create_user_mongo,
    create_product_mongo,
    create_order_mongo,
    register_user_mongo,
    login_mongo,
    get_products_mongo,
    get_orders_mongo
)


# ===================================================
# USER
# ===================================================

def create_user_service(data):

    if data["db"] == "mysql":
        return register_user_mysql(data)
    else:
        return create_user_mongo(data)


def register_service(data):

    if data["db"] == "mysql":
        return register_user_mysql(data)
    else:
        return register_user_mongo(data)


def login_service(data):

    if data["db"] == "mysql":
        return login_mysql(data)
    else:
        return login_mongo(data)


# ===================================================
# PRODUCT
# ===================================================

def create_product_service(data):

    if data["db"] == "mysql":
        return create_product_mysql(data)
    else:
        return create_product_mongo(data)


def get_products_service(db):

    if db == "mysql":
        return get_products_mysql()
    else:
        return get_products_mongo()


# ===================================================
# ORDER
# ===================================================

def create_order_service(data):

    if data["db"] == "mysql":
        return create_order_mysql(data)
    else:
        return create_order_mongo(data)


def get_orders_service(db):

    if db == "mysql":
        return get_orders_mysql()
    else:
        return {"message": "Mongo orders fetch optional"}