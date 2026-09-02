from .database import get_connection

def process_text_service(original_text: str):
    processed = original_text.upper()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (original, processed) VALUES (?, ?)",
        (original_text, processed)
    )

    conn.commit()
    conn.close()

    return processed
