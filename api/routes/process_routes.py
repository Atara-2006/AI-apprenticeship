
from fastapi import APIRouter, HTTPException
from ..models.text_input import TextInput
from ..services.process_service import process_text_service

router = APIRouter()

@router.post("/process")
def process_text(input: TextInput):
    try:
        processed = process_text_service(input.text)
        return {"original": input.text, "processed": processed}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
