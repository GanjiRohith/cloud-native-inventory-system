import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Database credentials - use environment variables without defaults for sensitive data
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST", "localhost")
    database = os.getenv("MYSQL_DB", "inventory_db")
    
    # Validate required credentials are present
    if not user or not password:
        raise ValueError(
            "MYSQL_USER and MYSQL_PASSWORD environment variables must be set. "
            "Please configure these in your .env file."
        )

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{user}:{password}@{host}/{database}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)