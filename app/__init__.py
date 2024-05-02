"""app/__init__.py Module"""

from flask import Flask
from config.database import db

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('config.settings')

    # Initialize database
    db.init_app(app)

    # Import blueprints
    from app.routes import user, appointment

    # Register blueprints
    app.register_blueprint(user.bp)
    app.register_blueprint(appointment.bp)

    return app
