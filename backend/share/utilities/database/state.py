from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from core.db_core import State
from utilities.log_controler import LogControler

log_controler = LogControler()

class State_Base(BaseModel):
    id: int
    name: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

def create_state_table(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_State = State(
            name=data.name
        )
        db_session.add(payload_State)
        db_session.flush()
        result = {"detail": "State added successfully", "data": State_Base(**payload_State.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "fill_state_table")
        result = {"error_server": "01", "msg": "fill_state_table: " + str(e)}

    return result

def update_state_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_State = db_session.query(State).filter(State.id == data.id).first()
        payload_State.name = data.name
    except Exception as e:
        log_controler.log_error(str(e), "update_state_table_by_id")
        result = {"error_server": "01", "msg": "update_state_table_by_id: " + str(e)}

    return result

def delete_state_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_State = db_session.query(State).filter(State.id == data.id).first()
        db_session.delete(payload_State)
    except Exception as e:
        log_controler.log_error(str(e), "delete_state_table_by_id")
        result = {"error_server": "01", "msg": "delete_state_table_by_id: " + str(e)}

    return result

def read_state_table_by_condition(data, db_session):
    """
        By id
        By name
        By created_at
        By updated_at
    """

    result = {"error_server": "00", "msg": "Server error"}
    try:
        if data.id:
            payload_State = db_session.query(State).filter(State.id == data.id).first()
        elif data.name:
            payload_State = db_session.query(State).filter(State.name == data.name).first()
        elif data.created_at:
            payload_State = db_session.query(State).filter(State.created_at == data.created_at).all()
        elif data.updated_at:
            payload_State = db_session.query(State).filter(State.updated_at == data.updated_at).all()
        else:
            payload_State = db_session.query(State).all()

        if payload_State:
            result = {"detail": "State read successfully", "data": [State_Base(**payload_State.__dict__) for payload_State in payload_State]}
        else:
            result = {"detail": "State not found", "data": []}
    except Exception as e:
        log_controler.log_error(str(e), "read_state_table_by_condition")
        result = {"error_server": "01", "msg": "read_state_table_by_condition: " + str(e)}

    return result