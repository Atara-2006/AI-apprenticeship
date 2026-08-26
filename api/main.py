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
