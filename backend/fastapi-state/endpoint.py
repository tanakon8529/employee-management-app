
from fastapi import APIRouter
from routes import state

api_router = APIRouter()

api_router.include_router(
    state.router, 
    prefix="", 
    tags=["state"]
)