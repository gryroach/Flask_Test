import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    with app.app_context():
        # Include Routes
        from .api import routes

        migrate.init_app(app, db)

        @app.shell_context_processor
        def ctx():
            return {'app': app, 'db': db}

        return app
