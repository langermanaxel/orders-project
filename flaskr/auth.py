import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from datetime import timedelta

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.get("/login")
def login_form():
    return render_template("login.html")

@bp.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == os.getenv("ADMIN_USER") and password == os.getenv("ADMIN_PASSWORD"):
        access_token = create_access_token(identity=username, expires_delta=timedelta(hours=8))
        resp = make_response(redirect(url_for("admin.dashboard")))
        set_access_cookies(resp, access_token)
        flash("Sesión iniciada correctamente.", "success")
        return resp

    flash("Credenciales incorrectas", "error")
    return redirect(url_for("auth.login_form"))

@bp.post("/logout")
def logout():
    resp = make_response(redirect(url_for("routes.menu")))
    unset_jwt_cookies(resp)
    flash("Sesión cerrada.", "success")
    return resp
