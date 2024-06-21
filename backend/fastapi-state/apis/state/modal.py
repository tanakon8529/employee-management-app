
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DynamicBaseModel(BaseModel):
    class Config:
        extra = 'allow'

class State_Form(DynamicBaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None