import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)

    # Instance dir para la DB
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'flaskr.sqlite')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY", "jwt-secret"),
        # JWT en cookies para proteger el panel admin de forma simple
        JWT_TOKEN_LOCATION=["cookies"],
        JWT_COOKIE_SECURE=False,           # True si usás HTTPS
        JWT_COOKIE_CSRF_PROTECT=False,     # Para simplificar en dev
        JWT_ACCESS_COOKIE_PATH="/",        # Cookie válida en toda la app
    )

    # Config extra desde config.py si existe
    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    jwt.init_app(app)

    # Blueprints
    from . import routes, auth, admin
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

    # CLI: init-db (crea tablas + seed)
    @app.cli.command("init-db")
    def init_db_command():
        from .models import Product
        with app.app_context():
            db.create_all()
            if not Product.query.first():
                demo = [
                    Product(name="Latte mediano", price=5500, category="Café"),
                    Product(name="Cappuccino mediano", price=5500, category="Café"),
                    Product(name="Muffin pera y chocolate", price=4200, category="Pastelería"),
                    Product(name="Alfajor de coco y dulce de leche", price=4500, category="Pastelería"),
                    Product(name="Agua chica", price=2000, category="Bebidas"),
                ]
                db.session.add_all(demo)
                db.session.commit()
                print("Base creada y productos demo agregados.")
            else:
                print("Base ya tenía datos; no se agregaron productos.")

    return app
