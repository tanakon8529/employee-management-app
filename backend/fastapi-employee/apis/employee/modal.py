
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DynamicBaseModel(BaseModel):
    class Config:
        extra = 'allow'

class Employee_Form(DynamicBaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    position_id: Optional[int] = None
    address: Optional[str] = None
    manager_id: Optional[int] = None
    image: Optional[str] = None
    state_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None