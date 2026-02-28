from src.config.db import db


class Inventory(db.Model):

    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.Integer,
        unique=True,   # VERY IMPORTANT
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )