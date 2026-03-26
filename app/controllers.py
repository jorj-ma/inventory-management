from .models import users

def register_user(username, password, role="viewer"):
    if any(u["username"] == username for u in users):
        return None, "Username already exists"
    new_id = max([u["id"] for u in users]) + 1 if users else 1
    new_user = {"id": new_id, "username": username, "password": password, "role": role}
    users.append(new_user)
    return new_user, None

def login_user(username, password):
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)
    return user
