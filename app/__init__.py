from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    migrate.init_app(app, db)


    @app.route('/')
    def index():
        return "healthy"

    with app.app_context():
        from .routes import register_routes
        register_routes(app)

        return app
