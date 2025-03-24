from flask import Blueprint, render_template, request, session
from uuid import uuid4

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if "users" not in session:
        session["users"] = []

    if request.method == "POST":
        user_data = {
            "id": str(uuid4()),  # Уникальный ID (если нужно будет удаление и т.п.)
            "name": request.form.get("name"),
            "city": request.form.get("city"),
            "hobby": request.form.get("hobby"),
            "age": request.form.get("age")
        }
        users = session["users"]
        users.append(user_data)
        session["users"] = users

    return render_template("blog.html", users=session.get("users", []))
