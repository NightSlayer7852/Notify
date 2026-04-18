from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title = "Notes Agent API",
    description = "Multi-Agent AI notes generator",
    version = "1.0"
)

app.include_router(router)