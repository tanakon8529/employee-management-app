from __future__ import annotations

from typing import Optional
from fastapi import APIRouter, Depends, Header
from core.auth import valid_access_token
from middlewares.middleware_db import db

from apis.state.mainmod import state_get, state_post, state_put, state_delete
from apis.state.modal import State_Form

router = APIRouter()

@router.post("/v1/")
async def post_state(
    data: State_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return state_post(data, db_session=db_session)

@router.get("/v1/")
async def get_state(
    data: Optional[State_Form] = None,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return state_get(data, db_session=db_session)

@router.put("/v1/")
async def put_state(
    data: State_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return state_put(data, db_session=db_session)

@router.delete("/v1/")
async def delete_state(
    data: State_Form,
    token: str = Depends(valid_access_token)
):
    db_session = db.session
    return state_delete(data, db_session=db_session)
