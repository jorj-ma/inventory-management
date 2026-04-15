from flask import Blueprint, request
from app.controllers.controllers import register_user, login_user, get_inventory_controller,add_item_controller, update_item_controller,delete_item_controller
from app.views.views import user_registered_view, login_view, inventory_view,item_added_view,item_updated_view, item_deleted_view

auth_bp = Blueprint("auth", __name__)
inventory_bp = Blueprint("inventory", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username, password, role_name = data.get("username"), data.get("password"), data.get("role_name")
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
    data = request.get_json()
    inventory_data, error = get_inventory_controller(data)
    return inventory_view(inventory_data, error)

@inventory_bp.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()
    result, error = add_item_controller(data)
    return item_added_view(result, error)

@inventory_bp.route("/inventory/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    result, error = update_item_controller(item_id, data)
    return item_updated_view(result, error)

@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    data = request.get_json()
    result, error = delete_item_controller(item_id, data)
    return item_deleted_view(error)