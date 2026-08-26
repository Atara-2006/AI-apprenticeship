import sqlite3

def get_connection():
    conn = sqlite3.connect("app.db")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original TEXT,
            processed TEXT
        )
    """)

    conn.commit()
    conn.close()
