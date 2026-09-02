from fastapi import APIRouter, HTTPException
from ..services.logs_service import get_all_logs_service, get_log_by_id_service

router = APIRouter()

@router.get("/logs")
def get_logs():
    return {"logs": get_all_logs_service()}


@router.get("/logs/{log_id}")
def get_log_by_id(log_id: int):
    if log_id <= 0:
        raise HTTPException(status_code=400, detail="log_id must be positive")

    row = get_log_by_id_service(log_id)

    if row is None:
        raise HTTPException(status_code=404, detail=f"log with id {log_id} not found")

    return {"log": row}
