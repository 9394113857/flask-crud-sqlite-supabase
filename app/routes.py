from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models import User

main = Blueprint("main", __name__)

# READ
@main.route("/")
def index():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template("index.html", users=users)

# CREATE
@main.route("/users", methods=["POST"])
def create_user():
    user = User(
        full_name=request.form["full_name"],
        email=request.form["email"],
        phone=request.form["phone"],
        age=request.form.get("age") or None,
        gender=request.form.get("gender")
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("main.index"))

# UPDATE (AJAX)
@main.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    user.full_name = data["full_name"]
    user.email = data["email"]
    user.phone = data["phone"]
    user.age = data.get("age")
    user.gender = data.get("gender")

    db.session.commit()
    return jsonify({"message": "updated"})

# DELETE (POST only, safe)
@main.route("/users/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("main.index"))
