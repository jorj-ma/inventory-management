from app.models.models import User, Role, Inventory
from werkzeug.security import check_password_hash
from flask import jsonify
from app.views.views import authenticate


def register_user(username, password, role_name):
    role = Role.get_by_name(role_name)
    if not role:
        return None, {"message": f"Role '{role_name}' not found"}

    if User.get_by_username(username):
        return None, {"message": "Username already exists"}

    user = User.create(username, password, role["id"])
    return {"id": user["id"], "username": user["username"], "role": role["name"]}, None


def login_user(username, password):
    user = User.get_by_username(username)
    if not user or not check_password_hash(user["password"], password):
        return None
    role = Role.get_by_id(user["role_id"])
    return {"id": user["id"], "username": user["username"], "role": role["name"]}


def get_inventory_controller(data):
    username, password = data.get("username"), data.get("password")
    user = authenticate(username, password)
    if not user:
        return None, {"message": "Invalid credentials"}
    return Inventory.all(), None

def add_item_controller(data):
    username, password = data.get("username"), data.get("password")
    item, quantity = data.get("item"), data.get("quantity")

    user = authenticate(username, password)
    if not user:
        return None, {"message": "Invalid credentials"}
    if user["role"] not in ["staff", "admin"]:
        return None, {"message": "Permission denied"}

    Inventory.add(item, quantity)
    return {"item": item, "quantity": quantity}, None

def update_item_controller(item_id, data):
    username, password = data.get("username"), data.get("password")
    quantity = data.get("quantity")

    user = authenticate(username, password)
    if not user:
        return None, {"message": "Invalid credentials"}
    if user["role"] not in ["staff", "admin"]:
        return None, {"message": "Permission denied"}

    updated = Inventory.update(item_id, quantity)
    if not updated:
        return None, {"message": "Item not found"}
    return updated, None

def delete_item_controller(item_id, data):
    username, password = data.get("username"), data.get("password")

    user = authenticate(username, password)
    if not user:
        return None, {"message": "Invalid credentials"}
    if user["role"] != "admin":
        return None, {"message": "Permission denied"}

    deleted = Inventory.delete(item_id)
    if not deleted:
        return None, {"message": "Item not found"}
    return None, None