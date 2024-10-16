from flask import Blueprint, render_template, request, redirect, url_for


bp = Blueprint("main", __name__)
@bp.route("/")

def index():
    return render_template("index.html")

@bp.route("/users")
def lista():
    return render_template("users.html")