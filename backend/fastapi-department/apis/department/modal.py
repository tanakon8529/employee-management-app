
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DynamicBaseModel(BaseModel):
    class Config:
        extra = 'allow'

class Department_Form(DynamicBaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    manager_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None