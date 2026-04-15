import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create roles table
cursor.execute("""
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role_id INTEGER,
    FOREIGN KEY(role_id) REFERENCES roles(id)
)
""")

# Insert default roles
cursor.executemany("INSERT OR IGNORE INTO roles (name) VALUES (?)", 
                   [("admin",), ("staff",), ("viewer",)])

conn.commit()
conn.close()
