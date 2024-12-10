from app.v1.routes import v1_bp
from flask import Flask

from extensions import init_extensions


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    # Initialize extensions
    init_extensions(app)

    return app
