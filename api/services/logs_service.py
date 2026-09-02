from .database import get_connection


def get_all_logs_service():
    """
    Retrieve all logs from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        rows = cursor.execute("SELECT * FROM logs").fetchall()
        return rows
    finally:
        conn.close()


def get_log_by_id_service(log_id: int):
    """
    Retrieve a single log by ID.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        row = cursor.execute(
            "SELECT * FROM logs WHERE id = ?",
            (log_id,)
        ).fetchone()
        return row
    finally:
        conn.close()


def update_log_state_service(log_id: int, state: str):
    """
    Update the state of a log record.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE logs SET state = ? WHERE id = ?",
            (state, log_id)
        )
        conn.commit()
    finally:
        conn.close()
