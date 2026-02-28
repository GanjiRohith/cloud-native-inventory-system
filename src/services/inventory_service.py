from src.config.db import db
from src.models.inventory import Inventory


def add_inventory_mysql(product_id, quantity):

    inventory = Inventory.query.filter_by(
        product_id=product_id
    ).first()

    if inventory:
        inventory.quantity += quantity
    else:
        inventory = Inventory(
            product_id=product_id,
            quantity=quantity
        )
        db.session.add(inventory)

    db.session.commit()

    print("✅ INVENTORY CREATED")