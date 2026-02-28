import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):

    user = os.getenv("MYSQL_USER","root")
    password = os.getenv("MYSQL_PASSWORD","root")
    host = os.getenv("MYSQL_HOST","localhost")
    database = os.getenv("MYSQL_DB","inventory")

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{user}:{password}@{host}/{database}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)