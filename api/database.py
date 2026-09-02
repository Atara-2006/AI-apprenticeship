import sqlite3

DB_PATH = "app.db"


def get_connection():
    """
    Create and return a new SQLite connection.
    """
    return sqlite3.connect(DB_PATH)


def init_db():
    """
    Initialize the database and create required tables.
    This runs once when the app starts.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original TEXT,
                processed TEXT,
                state TEXT
            )
        """)
        conn.commit()
    finally:
        conn.close()
