from fastapi import APIRouter, HTTPException
from ..services.logs_service import (
    get_all_logs_service,
    get_log_by_id_service,
    update_log_state_service
)

router = APIRouter()


@router.get("/logs")
def get_logs():
    """
    Retrieve all logs from the database.
    """
    try:
        logs = get_all_logs_service()
        return {"logs": logs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"database error: {str(e)}")


@router.get("/logs/{log_id}")
def get_log_by_id(log_id: int):
    """
    Retrieve a single log by ID.
    """
    if log_id <= 0:
        raise HTTPException(status_code=400, detail="log_id must be positive")

    row = get_log_by_id_service(log_id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"log {log_id} not found")

    return {"log": row}


@router.post("/logs/{log_id}/state")
def update_log_state(log_id: int, state: str):
    """
    Update the state of a log record.
    """
    valid_states = [
        "planned", "ready", "in_progress", "blocked",
        "needs_review", "done", "archived"
    ]

    if state not in valid_states:
        raise HTTPException(status_code=400, detail="invalid state")

    row = get_log_by_id_service(log_id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"log {log_id} not found")

    try:
        update_log_state_service(log_id, state)
        return {"id": log_id, "new_state": state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"database error: {str(e)}")
