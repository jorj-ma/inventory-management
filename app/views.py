from flask import jsonify

def user_registered_view(user, error=None):
    if error:
        return jsonify({"error": error}), 400
    return jsonify({
        "message": "Userregistered successfully",
        "user": user
    }), 201

def login_view(user):
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({
        "message": "Login successful",
        "user": user
    }), 200

def inventory_view(data, error=None):
    if error:
        # Decide error code based on message
        if error.get("message") == "Invalid credentials":
            return jsonify({"error": error}), 401
        else:
            return jsonify({"error": error}), 403
    return jsonify({
        "message": "Inventory retrieved successfully",
        "data": data
    }), 200
