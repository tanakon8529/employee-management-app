
from fastapi import APIRouter
from routes import position

api_router = APIRouter()

api_router.include_router(
    position.router, 
    prefix="", 
    tags=["position"]
)