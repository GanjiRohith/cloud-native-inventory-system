from flask import Flask
from src.config.db import db, init_db
from src.routes.user_routes import user_bp
from src.routes.product_routes import product_bp
from src.routes.order_routes import order_bp
from flask import send_from_directory
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")

init_db(app)

app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)


@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:path>")
def serve_frontend(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route("/health")
def health():
    return {"status": "OK"}


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)