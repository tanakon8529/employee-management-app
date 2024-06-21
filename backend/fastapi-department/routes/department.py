from __future__ import annotations

from typing import Optional
from fastapi import APIRouter, Depends, Header
from core.auth import valid_access_token
from middlewares.middleware_db import db

from apis.department.mainmod import department_get, department_post, department_put, department_delete
from apis.department.modal import Department_Form

router = APIRouter()

@router.post("/v1/")
async def post_department(
    data: Department_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return department_post(data, db_session=db_session)

@router.get("/v1/")
async def get_department(
    data: Optional[Department_Form] = None,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return department_get(data, db_session=db_session)

@router.put("/v1/")
async def put_department(
    data: Department_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return department_put(data, db_session=db_session)

@router.delete("/v1/")
async def delete_department(
    data: Department_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return department_delete(data, db_session=db_session)
