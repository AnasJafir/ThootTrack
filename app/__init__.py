"""app/__init__.py Module"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.database import Config

db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from app.controllers.user_controller import bp as user_bp
    from app.controllers.appointment_controller import bp as appointment_bp
    from app.controllers.patient_controller import bp as patient_bp


    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(patient_bp)

    return app
