from .database import get_connection


def process_text_service(original_text: str):
    """
    Deterministic processing service:
    - Converts text to uppercase
    - Stores original + processed + initial state in DB
    - Returns processed text
    """

    processed = original_text.upper()

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO logs (original, processed, state) VALUES (?, ?, ?)",
            (original_text, processed, "planned")
        )
        conn.commit()
    finally:
        conn.close()

    return processed
