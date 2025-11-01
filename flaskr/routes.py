import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product, Order
from .telegram import send_telegram_message

bp = Blueprint("routes", __name__)

@bp.get("/")
def menu():
    products = Product.query.order_by(Product.category, Product.name).all()
    return render_template("menu.html", products=products)

@bp.post("/order")
def order():
    name = request.form.get("name", "").strip()
    tel = request.form.get("tel", "").strip()  # 🆕 Nuevo campo

    # Validaciones
    if not name:
        flash("Ingresá tu nombre.", "error")
        return redirect(url_for("routes.menu"))

    if not tel:
        flash("Ingresá tu número de contacto.", "error")
        return redirect(url_for("routes.menu"))

    products = Product.query.all()
    items = []
    total = 0.0

    for p in products:
        qty_str = request.form.get(f"qty_{p.id}", "0").strip()
        try:
            qty = int(qty_str) if qty_str else 0
        except ValueError:
            qty = 0

        if qty > 0:
            subtotal = p.price * qty
            total += subtotal
            items.append({
                "id": p.id,
                "name": p.name,
                "qty": qty,
                "price": p.price,
                "subtotal": subtotal
            })

    if not items:
        flash("No seleccionaste productos.", "error")
        return redirect(url_for("routes.menu"))

    # 🆕 Guardar el teléfono junto con el pedido (si tu modelo lo permite)
    order = Order(
        customer_name=name,
        customer_tel=tel,  # nuevo campo en tu modelo Order
        items_json=json.dumps(items, ensure_ascii=False),
        total=round(total, 2)
    )
    db.session.add(order)
    db.session.commit()

    # 🆕 Incluir el número en el mensaje de Telegram
    lines = [
        f"🆕 Nuevo pedido #{order.id} de {name}",
        f"📞 Tel: {tel}",
        *(f"• {it['name']} x{it['qty']} = ${it['subtotal']:.0f}" for it in items),
        f"TOTAL: ${order.total:.0f}"
    ]
    send_telegram_message("\n".join(lines))

    flash("¡Pedido enviado! Te avisamos cuando esté listo.", "success")
    return redirect(url_for("routes.menu"))

