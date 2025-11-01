import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# ⚙️ Crear app mínima usando tu configuración real
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'flaskr.sqlite')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

# 🧩 Función auxiliar para agregar columnas si no existen
def add_column_if_not_exists(table_name, column_name, column_type):
    with db.engine.connect() as conn:
        # Usar comillas dobles para evitar error con nombres reservados
        result = conn.execute(text(f'PRAGMA table_info("{table_name}")')).fetchall()
        columns = [r[1] for r in result]
        if column_name not in columns:
            print(f"➡️  Agregando columna '{column_name}' a '{table_name}'...")
            conn.execute(text(f'ALTER TABLE "{table_name}" ADD COLUMN {column_name} {column_type}'))
            conn.commit()
        else:
            print(f"✅ La columna '{column_name}' ya existe en '{table_name}'.")

# 🧰 Ejecutar migraciones necesarias
def migrate():
    print("🚀 Iniciando migración de base de datos...")

    # Ejemplo actual: agregar customer_tel
    add_column_if_not_exists("order", "customer_tel", "VARCHAR(20)")

    # Podés agregar más en el futuro:
    # add_column_if_not_exists("order", "status", "VARCHAR(20)")
    # add_column_if_not_exists("product", "available", "BOOLEAN")

    print("✅ Migración completada con éxito.")

if __name__ == "__main__":
    with app.app_context():
        migrate()
