import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, inspect
from flaskr.models import Order, Product  # importa tus modelos reales

# Crear app básica para acceder al contexto de la DB
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'flaskr.sqlite')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


def get_declared_columns(model):
    """Devuelve un diccionario con columnas definidas en el modelo SQLAlchemy."""
    return {col.name: str(col.type) for col in model.__table__.columns}


def get_existing_columns(table_name):
    """Devuelve un listado de columnas existentes en la tabla SQLite."""
    with db.engine.connect() as conn:
        result = conn.execute(text(f'PRAGMA table_info("{table_name}")')).fetchall()
        return [r[1] for r in result]


def add_missing_columns(model, table_name):
    """Compara columnas declaradas vs existentes y agrega las faltantes."""
    declared = get_declared_columns(model)
    existing = get_existing_columns(table_name)

    with db.engine.connect() as conn:
        for col_name, col_type in declared.items():
            if col_name not in existing:
                print(f"➡️  Agregando columna '{col_name}' a '{table_name}' ({col_type})...")
                conn.execute(text(f'ALTER TABLE "{table_name}" ADD COLUMN {col_name} {col_type}'))
        conn.commit()


def migrate():
    print("🚀 Iniciando migración automática de base de datos...\n")

    # 🔧 Lista de modelos a sincronizar
    models = {
        "order": Order,
        "product": Product,
    }

    for table, model in models.items():
        print(f"🔍 Revisando tabla '{table}'...")
        add_missing_columns(model, table)
        print(f"✅ Tabla '{table}' sincronizada.\n")

    print("🎉 Migración completada con éxito.")


if __name__ == "__main__":
    with app.app_context():
        migrate()
