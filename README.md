📖 Inventory Management API Documentation
This API provides user authentication and inventory management with role‑based permissions.


Clone the repo. Navigate into directory. Create and activate virtual environment($Python -m venv venv  $source venv/bin/activate). Run command to install everything in the requirements.txt file(pip install -r requirements.txt) run the following commands:
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

Roles:

Viewer → read‑only access

Staff → can add and update items

Admin → full CRUD (create, read, update, delete)

USING POSTMAN
>>>Authentication
    -----REGISTER USER-----
POST .../auth/register

    json
    {
    "username": "Thende",
    "password": "Clown",
    "role_name": "admin"
    }
Response (201)

json
    {
    "status": "success",
    "message": "User registered successfully",
    "data": {
        "id": 1,
        "username": "Thende",
        "role": "admin"
    }
    }


    -----LOGIN USER-----
POST .../auth/login

json
    {
    "username": "Thende",
    "password": "Clown"
    }
Response (200)

json
    {
    "status": "success",
    "message": "Login successful",
    "data": {
        "id": 1,
        "username": "Thende",
        "role": "admin"
    }
    }


>>>Inventory
    -----VIEW INVENTORY-----
GET .../auth/inventory

json
    {
    "username": "Thende",
    "password": "Clown"
    }
Response (200)

json
    {
        "data": [
            {
                "id": 1,
                "item": "Mouse",
                "quantity": 15
            },
            {
                "id": 2,
                "item": "Keyboard",
                "quantity": 20
            }
        ],
        "message": "Inventory retrieved successfully",
        "status": "success"
    }

    -----ADD ITEM (staff/admin only)-----
POST .../auth/inventory

json
    {
    "username": "Thende",
    "password": "Clown",
    "item": "Keyboard",
    "quantity": 20
    }
Response (201)

json
    {
    "status": "success",
    "message": "Item 'Keyboard' added successfully",
    "data": {
        "item": "Keyboard",
        "quantity": 20
    }
    }

    -----UPDATE ITEM (staff/admin only)-----
PUT .../auth/inventory/<id>

json
    {
    "username": "Thende",
    "password": "Clown",
    "quantity": 25
    }
Response (200)

json
    {
    "status": "success",
    "message": "Item updated successfully",
    "data": {
        "id": 1,
        "item": "Mouse",
        "quantity": 25
    }
    }


    -----DELETE ITEM (admin only)-----
DELETE .../auth/inventory/<id>

json
    {
    "username": "Thende",
    "password": "Clown"
    }
Response (200)

json
    {
    "status": "success",
    "message": "Item deleted successfully",
    "data": null
    }


🔹 Role Permissions
Viewer → GET /auth/inventory

Staff → GET, POST, PUT

Admin → GET, POST, PUT, DELETE