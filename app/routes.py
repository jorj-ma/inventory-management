from flask import Blueprint, request,jsonify
from .controllers import register_user, login_user
from .views import user_registered_view, login_view
import sqlite3

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username,password,role_name=data.get("username"),data.get("password"),data.get("role","viewer")
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()

    #check if role entered exists
    cursor.execute("SELECT id FROM roles WHERE name=?",(role_name,))
    role=cursor.fetchone()
    if not role:
        return {"error": {"message": f"Role '{role_name} not found"}}, 400
    
    #check if username exists
    cursor.execute("SELECT id FROM users WHERE username=?", (username,))
    if cursor.fetchone():
        return{"error":{"message":"Usernamea lready exists"}}, 400
    
    #insert new user
    cursor.execute("INSERT INTO users(username, password, role_id) VALUES(?,?,?)"
                   ,(username,password,role[0]))
    conn.commit()
    user_id=cursor.lastrowid
    conn.close()
    return {"message":"User registered succesfully",
            "user":{"id": user_id,"username":username,"role":role_name}}, 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username, password = data.get("username"), data.get("password")

    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()

    cursor.execute("""
                   SELECT users.id, users.username,roles.name
                   FROM users JOIN roles ON users.role_id=roles.id
                   WHERE users.username=? AND users.password=?
                   """, (username, password))
    user=cursor.fetchone()
    conn.close()

    if not user:
        return {"error": {"message":"Invalid Credentials"}}, 401
    return {"message": "Login successful","user":{"id": user[0], "username":user[1],"role":user[2]}}, 200


@auth_bp.route("/inventory", methods=["GET"])
def inventory():
    data = request.json
    username, password = data.get("username"), data.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT users.id, users.username, roles.name 
    FROM users JOIN roles ON users.role_id = roles.id
    WHERE users.username=? AND users.password=?
    """, (username, password))

    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error": {"message": "Invalid credentials"}}), 401

    # only staff or admin can access
    role = user[2]
    if role not in ["staff", "admin"]:
        return jsonify({"error": {"message": "Access denied", "allowed_roles": ["staff", "admin"]}}), 403

    # Demo inventory data
    inventory_data = [
        {"item": "Laptop", "quantity": 10},
        {"item": "Monitor", "quantity": 5},
        {"item": "Keyboard", "quantity": 20}
    ]

    return jsonify({"message": "Inventory retrieved successfully", "data": inventory_data}), 200
