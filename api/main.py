from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_connection, init_db

app = FastAPI()
init_db()

class TextInput(BaseModel):
    text: str

@app.post("/process")
def process_text(input: TextInput):
    processed = input.text.upper()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (original, processed) VALUES (?, ?)",
        (input.text, processed)
    )

    conn.commit()
    conn.close()

    return {"original": input.text, "processed": processed}

@app.get("/logs")
def get_logs():
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM logs").fetchall()

    conn.close()

    return {"logs": rows}


@app.get("/logs/{log_id}")
def get_log_by_id(log_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    row = cursor.execute(
        "SELECT * FROM logs WHERE id = ?",
        (log_id,)
    ).fetchone()

    conn.close()

    if row is None:
        return {"error": f"log with id {log_id} not found"}

    return {"log": row}
