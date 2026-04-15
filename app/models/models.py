import sqlite3

DB_PATH = "users.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

class Role:
    @staticmethod
    def get_by_name(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM roles WHERE name=?", (name,))
        row = cursor.fetchone()
        conn.close()
        return {"id": row[0], "name": row[1]} if row else None

    @staticmethod
    def get_by_id(role_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM roles WHERE id=?", (role_id,))
        row = cursor.fetchone()
        conn.close()
        return {"id": row[0], "name": row[1]} if row else None


class User:
    @staticmethod
    def get_by_username(username):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password, role_id FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        conn.close()
        return {"id": row[0], "username": row[1], "password": row[2], "role_id": row[3]} if row else None

    @staticmethod
    def create(username, password, role_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(username, password, role_id) VALUES(?,?,?)",
                       (username, password, role_id))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return {"id": user_id, "username": username, "role_id": role_id}
