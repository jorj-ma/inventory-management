from flask import Blueprint, request
from .controllers import register_user, login_user
from .views import user_registered_view, login_view

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user, error = register_user(data.get("username"), data.get("password"), data.get("role", "viewer"))
    return user_registered_view(user, error)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = login_user(data.get("username"), data.get("password"))
    return login_view(user)
