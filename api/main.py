from fastapi import FastAPI
from .database import init_db
from .routes.process_routes import router as process_router
from .routes.logs_routes import router as logs_router

app = FastAPI()
init_db()

app.include_router(process_router)
app.include_router(logs_router)
