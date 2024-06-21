
from fastapi import APIRouter
from routes import department

api_router = APIRouter()

api_router.include_router(
    department.router, 
    prefix="", 
    tags=["department"]
)