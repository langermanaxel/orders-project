import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, get_jwt_identity, verify_jwt_in_request
from dotenv import load_dotenv

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)

    # Crear carpeta instance para la DB
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # ⚙️ Configuración principal
    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret"),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'flaskr.sqlite')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,

        # JWT CONFIG
        JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY", "jwt-secret"),
        JWT_TOKEN_LOCATION=["cookies"],
        JWT_COOKIE_SECURE=False,           # True si usás HTTPS
        JWT_COOKIE_CSRF_PROTECT=False,     # En producción poner True
        JWT_ACCESS_COOKIE_PATH="/",        # Cookie válida en toda la app
        JWT_COOKIE_DOMAIN=None,            # Permite que se use entre blueprints
        JWT_SESSION_COOKIE=True,           # Persiste en la sesión del navegador
    )

    # Config extra desde config.py (si existe)
    app.config.from_pyfile("config.py", silent=True)

    # Inicialización
    db.init_app(app)
    jwt.init_app(app)

    # 🔹 Context processor para usar `{{ current_user }}` en templates
    @app.context_processor
    def inject_current_user():
        try:
            verify_jwt_in_request(optional=True)
            user = get_jwt_identity()
        except Exception:
            user = None
        return dict(current_user=user)

    # 🔹 Blueprints
    from . import routes, auth, admin
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

    # 🔹 CLI: inicializar DB
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

