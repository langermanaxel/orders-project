import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import jwt_required
from .models import db, Product, Order

bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.get("/")
@jwt_required()
def dashboard():
    products = Product.query.order_by(Product.category, Product.name).all()
    orders = Order.query.order_by(Order.created_at.desc()).limit(20).all()
    # Parse items para mostrar
    parsed_orders = []
    for o in orders:
        try:
            items = json.loads(o.items_json)
        except Exception:
            items = []
        parsed_orders.append((o, items))
    return render_template("admin.html", products=products, orders=parsed_orders)

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

@bp.post("/product/delete/<int:pid>")
@jwt_required()
def delete_product(pid):
    p = Product.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    flash("Producto eliminado.", "success")
    return redirect(url_for("admin.dashboard"))

@bp.post("/order/status/<int:oid>")
@jwt_required()
def update_order_status(oid):
    o = Order.query.get_or_404(oid)
    new_status = request.form.get("status", "pending")
    o.status = new_status
    db.session.commit()
    flash(f"Pedido #{oid} actualizado a '{new_status}'.", "success")
    return redirect(url_for("admin.dashboard"))
