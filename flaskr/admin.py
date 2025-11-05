import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required
from .models import db, Product, Order
from .telegram import send_telegram_message_to

bp = Blueprint("admin", __name__, url_prefix="/admin")

# 📊 Panel principal
@bp.get("/")
@jwt_required()
def dashboard():
    products = Product.query.order_by(Product.category, Product.name).all()
    orders = Order.query.order_by(Order.created_at.desc()).limit(20).all()
    parsed_orders = []
    for o in orders:
        try:
            items = json.loads(o.items_json)
        except Exception:
            items = []
        parsed_orders.append((o, items))
    return render_template("admin.html", products=products, orders=parsed_orders)


# ➕ Agregar producto
@bp.post("/product/add")
@jwt_required()
def add_product():
    name = request.form.get("name", "").strip()
    price = request.form.get("price", "").strip()
    category = request.form.get("category", "").strip() or None
    if not name or not price:
        flash("Nombre y precio son obligatorios.", "error")
        return redirect(url_for("admin.dashboard"))
    try:
        price_f = float(price)
    except ValueError:
        flash("Precio inválido.", "error")
        return redirect(url_for("admin.dashboard"))

    db.session.add(Product(name=name, price=price_f, category=category))
    db.session.commit()
    flash("Producto agregado.", "success")
    return redirect(url_for("admin.dashboard"))


# ❌ Eliminar producto
@bp.post("/product/delete/<int:pid>")
@jwt_required()
def delete_product(pid):
    p = Product.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    flash("Producto eliminado.", "success")
    return redirect(url_for("admin.dashboard"))


# 🔄 Actualizar estado del pedido + enviar notificación Telegram
@bp.post("/order/status/<int:oid>")
@jwt_required()
def update_order_status(oid):
    o = Order.query.get_or_404(oid)
    new_status = request.form.get("status", "pending")
    o.status = new_status
    db.session.commit()

    # 🔔 Notificar al cliente por Telegram
    if getattr(o, "customer_chat_id", None):
        status_msg = {
            "pending": "⏳ Tu pedido está pendiente.",
            "in_progress": "👨‍🍳 Tu pedido está en preparación.",
            "ready": "✅ ¡Tu pedido ya está listo para retirar!",
            "delivered": "🚚 Tu pedido fue entregado. ¡Gracias por tu compra!"
        }.get(new_status, f"🔔 Estado actualizado: {new_status}")

        msg = f"Hola {o.customer_name},\n{status_msg}\n(Pedido #{o.id})"
        send_telegram_message_to(msg, o.customer_chat_id)
    else:
        print(f"[Sin chat_id] No se pudo notificar al cliente {o.customer_name}")

    flash(f"Pedido #{oid} actualizado a '{new_status}'.", "success")
    return redirect(url_for("admin.dashboard"))
