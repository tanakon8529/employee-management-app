from __future__ import annotations

from typing import Optional
from fastapi import APIRouter, Depends, Header
from core.auth import valid_access_token
from middlewares.middleware_db import db

from apis.position.mainmod import position_get, position_post, position_put, position_delete
from apis.position.modal import Position_Form

router = APIRouter()

@router.post("/v1/")
async def post_position(
    data: Position_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return position_post(data, db_session=db_session)

@router.get("/v1/")
async def get_position(
    data: Optional[Position_Form] = None,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return position_get(data, db_session=db_session)

@router.put("/v1/")
async def put_position(
    data: Position_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return position_put(data, db_session=db_session)

@router.delete("/v1/")
async def delete_position(
    data: Position_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return position_delete(data, db_session=db_session)
