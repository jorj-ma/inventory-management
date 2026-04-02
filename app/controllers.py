from .models import User, Role

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
    if not user or user["password"] != password:
        return None
    role = Role.get_by_id(user["role_id"])
    return {"id": user["id"], "username": user["username"], "role": role["name"]}


def get_inventory(username, password):
    user = User.get_by_username(username)
    if not user or user["password"] != password:
        return None, {"message": "Invalid credentials"}

    role = Role.get_by_id(user["role_id"])
    if role["name"] not in ["staff", "admin"]:
        return None, {"message": "Access denied", "allowed_roles": ["staff", "admin"]}

    inventory_data = [
        {"item": "Laptop", "quantity": 10},
        {"item": "Monitor", "quantity": 5},
        {"item": "Keyboard", "quantity": 20}
    ]
    return inventory_data, None
