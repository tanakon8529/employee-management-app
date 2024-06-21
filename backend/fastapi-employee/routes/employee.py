from __future__ import annotations

from typing import Optional
from fastapi import APIRouter, Depends, Header
from core.auth import valid_access_token
from middlewares.middleware_db import db

from apis.employee.mainmod import employee_get, employee_post, employee_put, employee_delete
from apis.employee.modal import Employee_Form

router = APIRouter()

@router.post("/v1/")
async def post_employee(
    data: Employee_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return employee_post(data, db_session=db_session)

@router.get("/v1/")
async def get_employee(
    data: Optional[Employee_Form] = None,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return employee_get(data, db_session=db_session)

@router.get("/v1/signin/")
async def get_signin(
    data: Employee_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return employee_get(data, db_session=db_session, signin=True)

@router.put("/v1/")
async def put_employee(
    data: Employee_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return employee_put(data, db_session=db_session)

@router.delete("/v1/")
async def delete_employee(
    data: Employee_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return employee_delete(data, db_session=db_session)
