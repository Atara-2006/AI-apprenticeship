from .database import get_connection

def get_all_logs_service():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM logs").fetchall()
    conn.close()
    return rows


def get_log_by_id_service(log_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    row = cursor.execute("SELECT * FROM logs WHERE id = ?", (log_id,)).fetchone()
    conn.close()
    return row
