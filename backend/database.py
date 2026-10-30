import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "healthguard.db")


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            symptoms TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_user(age, symptoms):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (age, symptoms)
        VALUES (?, ?)
    """, (age, symptoms))

    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return users