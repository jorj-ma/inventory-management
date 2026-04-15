from flask import jsonify
from werkzeug.security import check_password_hash
from app.models.models import User
from app.models.models import Role

def api_response(data=None, message="Success", status="success", code=200):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), code

def api_error(message="Error", code=400):
    return jsonify({
        "status": "error",
        "message": message,
        "data": None
    }), code


def user_registered_view(user, error=None):
    if error:
        return api_error(error.get("message", "Registration failed"), 400)
    return api_response(user, "User registered successfully", "success", 201)


def login_view(user):
    if not user:
        return api_error("Invalid credentials", 401)
    return api_response(user, "Login successful", "success", 200)


def inventory_view(data, error=None):
    if error:
        msg = error.get("message")
        if msg == "Invalid credentials":
            return api_error("Invalid credentials", 401)
        elif msg == "Permission denied":
            return api_error("Permission denied", 403)
        elif msg == "Item not found":
            return api_error("Item not found", 404)
        return api_error(msg or "Access denied", 403)
    return api_response(data, "Inventory retrieved successfully", "success", 200)

def item_added_view(data, error=None):
    if error:
        return api_error(error.get("message", "Failed to add item"), 400)
    return api_response(data, f"Item '{data['item']}' added successfully", "success", 201)

def item_updated_view(data, error=None):
    if error:
        msg = error.get("message")
        if msg == "Item not found":
            return api_error("Item not found", 404)
        return api_error(msg or "Failed to update item", 400)
    return api_response(data, "Item updated successfully", "success", 200)

def item_deleted_view(error=None):
    if error:
        msg = error.get("message")
        if msg == "Item not found":
            return api_error("Item not found", 404)
        return api_error(msg or "Failed to delete item", 400)
    return api_response(None, "Item deleted successfully", "success", 200)

def authenticate(username, password):
    user = User.get_by_username(username)
    if not user or not check_password_hash(user["password"], password):
        return None
    role = Role.get_by_id(user["role_id"])
    return {**user, "role": role["name"]}