from flask import jsonify

def user_registered_view(user, error=None):
    if error:
        return jsonify({"error": error}), 400
    return jsonify({
        "message": "User registered successfully",
        "user": {"id": user["id"], "username": user["username"], "role": user["role"]}
    }), 201

def login_view(user):
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({
        "message": "Login successful",
        "role": user["role"]
    })
