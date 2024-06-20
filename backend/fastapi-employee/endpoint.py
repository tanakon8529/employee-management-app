
from fastapi import APIRouter
from routes import employee

api_router = APIRouter()

api_router.include_router(
    employee.router, 
    prefix="", 
    tags=["employee"]
)