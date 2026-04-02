from flask import Blueprint, request
from .controllers import register_user, login_user, get_inventory
from .views import user_registered_view, login_view, inventory_view

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username, password, role_name = data.get("username"), data.get("password"), data.get("role", "viewer")
    user, error = register_user(username, password, role_name)
    return user_registered_view(user, error)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username, password = data.get("username"), data.get("password")
    user = login_user(username, password)
    return login_view(user)


@auth_bp.route("/inventory", methods=["GET"])
def inventory():
    data = request.json
    username, password = data.get("username"), data.get("password")
    inventory_data, error = get_inventory(username, password)
    return inventory_view(inventory_data, error)
