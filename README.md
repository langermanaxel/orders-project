<div align="center">

# ☕ Orders Project  
### Sistema de Pedidos Online para Cafeterías  
Desarrollado con **Flask + SQLite + JWT + Telegram API**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405E?logo=sqlite)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 🌐 Descripción

**Orders Project** es una aplicación web pensada para cafeterías o negocios pequeños que buscan digitalizar sus pedidos.  
Los clientes pueden hacer pedidos desde la web, y el administrador los recibe en **Telegram** en tiempo real.  
Incluye panel de administración seguro, integración con JWT y un diseño adaptable modo claro/oscuro.  

---

## 🚀 Tecnologías principales

| Área | Tecnología |
|------|-------------|
| Backend | [Python 3](https://www.python.org/), [Flask](https://flask.palletsprojects.com/), [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/), [SQLAlchemy](https://www.sqlalchemy.org/) |
| Base de datos | SQLite |
| Frontend | HTML + CSS (modo oscuro y claro automático) |
| Integraciones | [Telegram Bot API](https://core.telegram.org/bots/api) |
| Configuración | Variables de entorno con `.env` |
| Entorno | CLI personalizada de Flask para inicializar la base |

---

## 🧱 Estructura del proyecto

```bash
orders-project/
├── flaskr/
│   ├── __init__.py         # Configuración de Flask, DB, JWT y Blueprints
│   ├── admin.py            # Panel admin: productos y pedidos
│   ├── auth.py             # Login / Logout con JWT (cookies seguras)
│   ├── routes.py           # Rutas públicas: menú, pedidos
│   ├── models.py           # Modelos de datos
│   ├── telegram.py         # Integración con la API de Telegram
│   ├── templates/          # Vistas HTML (Jinja2)
│   └── static/
│       └── style.css       # Diseño moderno, modo claro/oscuro
├── instance/
│   └── flaskr.sqlite       # Base de datos SQLite
├── migrate_db.py           # Script de migraciones sin pérdida de datos
├── run.py                  # Punto de entrada
├── .env.example            # Ejemplo de variables de entorno
└── README.md               # Este archivo 😎

⚙️ Instalación y configuración
1️⃣ Clonar el repositorio
git clone https://github.com/langermanaxel/orders-project.git
cd orders-project

2️⃣ Crear entorno virtual e instalar dependencias
python -m venv .venv
.venv\Scripts\activate  # (Windows)
pip install -r requirements.txt

3️⃣ Configurar variables de entorno

Creá un archivo .env en la raíz con tus credenciales:

SECRET_KEY=clave-secreta
JWT_SECRET_KEY=jwt-secreta
ADMIN_USER=admin
ADMIN_PASSWORD=1234
TELEGRAM_TOKEN=tu_token_de_bot
TELEGRAM_CHAT_ID=tu_chat_id


💡 El TELEGRAM_CHAT_ID puede ser el ID de tu chat personal o de un grupo donde quieras recibir pedidos.

4️⃣ Inicializar la base de datos
flask --app flaskr init-db

5️⃣ Ejecutar la aplicación
flask --app run.py run


🖥️ Luego abrí: http://127.0.0.1:5000/

👨‍💼 Funcionalidades principales
🧾 Cliente

Ver menú de productos.

Ingresar nombre y número de contacto.

Seleccionar productos y enviar pedido.

Confirmación visual con mensajes flash.

🧑‍🍳 Administrador

Login seguro con JWT (cookies).

Panel para gestionar productos y pedidos.

Actualización de estado del pedido:

⏳ Pendiente

👨‍🍳 En preparación

✅ Listo

🚚 Entregado

Notificaciones instantáneas al Telegram del administrador.

🤖 Integración con Telegram

Cada nuevo pedido dispara una notificación directa al bot del administrador.

Los mensajes incluyen:

Nombre del cliente ☕

Detalle del pedido 🍪

Total 💵

Plan futuro: enviar actualizaciones automáticas al cliente (vinculado por teléfono o chat_id).

🧩 Script de migración (migrate_db.py)

Permite agregar nuevos campos a la base de datos sin perder datos existentes.
Ideal para actualizaciones de modelos (por ejemplo: customer_tel, customer_chat_id, etc).

Uso:

python migrate_db.py

🧠 Próximas mejoras (Roadmap)

 Enviar actualizaciones de estado al cliente por Telegram.

 Historial de cambios por pedido.

 Tests unitarios para rutas y modelos.

 Soporte multiusuario (varios admins).

 Dockerfile y configuración de despliegue en Render.

 API REST pública (para integraciones externas).

🧰 Variables de entorno
Variable	Descripción
SECRET_KEY	Clave principal de Flask
JWT_SECRET_KEY	Clave secreta para JWT
ADMIN_USER / ADMIN_PASSWORD	Credenciales del panel admin
TELEGRAM_TOKEN	Token del bot de Telegram
TELEGRAM_CHAT_ID	Chat o grupo donde se envían los pedidos
🧑‍💻 Autor

Axel Langerman
📍 Río Gallegos / El Calafate, Argentina
💻 GitHub

☕ Desarrollador Backend y amante del café

<div align="center">

⭐ Si te gusta este proyecto, dejale una estrella en GitHub. ¡Ayuda muchísimo! ⭐

</div> ```
🪄 Detalles que podés sumar para hacerlo aún más visual:

Badges extra opcionales

![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-black?logo=flask)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)
![Built with Love](https://img.shields.io/badge/Built%20with-❤-red)


Capturas en /docs/
Si subís capturas (/docs/menu.png, /docs/admin.png, /docs/telegram.png), el README las mostrará en la sección de “📸 Capturas”.

.env.example
Incluí un archivo .env.example con valores vacíos para que otros puedan replicar tu entorno fácilmente.