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

## 📌 Elevator pitch (30-45s)
"OrdersApp es una aplicación web para cafeterías que permite recibir pedidos desde la web y notificar al administrador en Telegram en tiempo real. Está construida con Flask y SQLite, usa JWT para el panel de administración y está pensada para ser ligera, fácil de extender y desplegar."

---

## 🌐 Descripción

**Orders Project** es una aplicación web pensada para cafeterías o negocios pequeños que buscan digitalizar sus pedidos.  
Los clientes pueden hacer pedidos desde la web, y el administrador los recibe en **Telegram** en tiempo real.  
Incluye panel de administración seguro, integración con JWT y un diseño adaptable modo claro/oscuro.

---

## 🚀 Tecnologías principales

| Área | Tecnología |
|------|------------|
| Backend | Python 3.10+, Flask, Flask-JWT-Extended, SQLAlchemy |
| Base de datos | SQLite |
| Frontend | HTML + CSS (modo claro/oscuro) |
| Integraciones | Telegram Bot API |
| Configuración | Variables de entorno con `.env` / `.env.example` |
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
│   └── flaskr.sqlite       # Base de datos SQLite (no subir al repo)
├── migrate_db.py           # Script de migraciones sin pérdida de datos
├── run.py                  # Punto de entrada (recomendado: python run.py)
├── .env.example            # Ejemplo de variables de entorno
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación rápida (en 1–2 minutos)

1) Clonar el repositorio
```bash
git clone https://github.com/langermanaxel/orders-project.git
cd orders-project
```

2) Crear entorno virtual e instalar dependencias
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

3) Configurar variables de entorno

Copia `.env.example` a `.env` y completa los valores:
```
SECRET_KEY=clave-secreta
JWT_SECRET_KEY=jwt-secreta
ADMIN_USER=admin
ADMIN_PASSWORD=1234
TELEGRAM_TOKEN=tu_token_de_bot
TELEGRAM_CHAT_ID=tu_chat_id
```
Importante: NO subir `.env` al repositorio.

4) Inicializar la base de datos
```bash
# Si incluíste la CLI personalizada
flask --app flaskr init-db
# O usa el script/función de inicialización incluida (si existe)
python run.py --init-db
```

5) Ejecutar la aplicación (elige una opción según cómo expongas la app)
```bash
# Opción A - recomendado si run.py contiene el entrypoint
python run.py

# Opción B - si expones create_app en flaskr/__init__.py
# macOS / Linux
export FLASK_APP=flaskr
flask run
# Windows (PowerShell)
$env:FLASK_APP = "flaskr"
flask run
```

Luego abrí: http://127.0.0.1:5000/

---

## 🎯 Demo rápida (2–5 min) — pasos que voy a mostrar
1. Abrir la home: mostrar menú de productos.
2. Crear un pedido como cliente (completar nombre/telefono y seleccionar productos) → mostrar confirmación visual.
3. Entrar al panel de admin (login) → ver listado de pedidos.
4. Cambiar estado del pedido (Pendiente → En preparación → Listo → Entregado).
5. Mostrar la notificación recibida por el bot de Telegram (screenshot o chat en vivo).

> Consejo: Antes de la entrevista, deja el navegador abierto en la URL local y el editor con estos archivos: `run.py`, `flaskr/routes.py`, `flaskr/models.py`, `flaskr/templates/admin.html`.

---

## 👨‍💼 Funcionalidades principales

Cliente:
- Ver menú de productos.
- Ingresar nombre y número de contacto.
- Seleccionar productos y enviar pedido.
- Confirmación visual con mensajes flash.

Administrador:
- Login seguro con JWT (cookies).
- Panel para gestionar productos y pedidos.
- Actualización de estado del pedido: Pendiente → En preparación → Listo → Entregado.
- Notificaciones instantáneas al Telegram del administrador.

Integración con Telegram:
- Cada nuevo pedido dispara una notificación directa al bot del administrador.
- Mensajes incluyen nombre, detalle del pedido y total.

---

## 🧩 Migraciones

`migrate_db.py` permite agregar campos a la base de datos sin perder datos existentes. Uso:
```bash
python migrate_db.py
```

---

## 📸 Capturas (opcional pero recomendable)
Añadí capturas en `/docs/` y luego enlazalas aquí:
- /docs/menu.png
- /docs/admin.png
- /docs/telegram.png

Ejemplo en markdown:
```md
### 📸 Capturas
![Menú](/docs/menu.png)
![Admin](/docs/admin.png)
![Telegram](/docs/telegram.png)
```

---

## 🧠 Roadmap / Próximas mejoras
- Enviar actualizaciones de estado al cliente por Telegram.
- Historial de cambios por pedido.
- Tests unitarios para rutas y modelos.
- Soporte multiusuario (varios admins).
- Dockerfile y despliegue en Render / Heroku.
- API REST pública (para integraciones externas).

---

## 🔒 Seguridad y buenas prácticas
- No subir nunca `.env` con credenciales.
- Validación y sanitización de entrada en servidor.
- Escapar contenido en plantillas Jinja2 (ya aplicado en templates críticas).
- Para produccion: configurar HTTPS y revisar políticas de CORS.

---

## 🧰 Variables de entorno (resumen)

| Variable | Descripción |
|----------|-------------|
| SECRET_KEY | Clave principal de Flask |
| JWT_SECRET_KEY | Clave secreta para JWT |
| ADMIN_USER / ADMIN_PASSWORD | Credenciales del panel admin (temporal para demo) |
| TELEGRAM_TOKEN | Token del bot de Telegram |
| TELEGRAM_CHAT_ID | Chat o grupo donde se envían los pedidos |

---

## 🧪 Tests
(Actualmente en roadmap) — cuando agregues tests, incluye aquí cómo ejecutarlos:
```bash
pytest
```

---

## 🤝 Contribuir
PRs bienvenidos. Para cambios grandes, abrí un issue antes para discutir el diseño.

---

## 📜 Licencia
MIT (añadir archivo LICENSE si aún no está).

---

## 🧑‍💻 Autor
Axel Langerman  
📍 Río Gallegos / El Calafate, Argentina  
GitHub: [langermanaxel](https://github.com/langermanaxel)

<div align="center">
⭐ Si te gusta este proyecto, dejale una estrella en GitHub. ¡Ayuda muchísimo! ⭐
</div>
