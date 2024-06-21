from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from core.db_core import State
from utilities.log_controler import LogControler
from utilities.time_controler import get_current_date

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
            name=data.name,
            created_at=get_current_date(),
            updated_at=None
        )
        db_session.add(payload_State)
        db_session.flush()
        result = {"detail": "State added successfully", "data": State_Base(**payload_State.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "fill_State_table")
        result = {"error_server": "01", "msg": "fill_State_table: " + str(e)}

    return result

def update_state_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_State = db_session.query(State).filter(State.id == data.id).first()
        if not payload_State:
            return {"error_server": "01", "msg": "State not found"}
        
        payload_State.name = data.name
        payload_State.updated_at = get_current_date()
        db_session.flush()
        result = {"detail": "State updated successfully", "data": State_Base(**payload_State.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "update_State_table_by_id")
        result = {"error_server": "01", "msg": "update_State_table_by_id: " + str(e)}

    return result

def delete_state_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_State = db_session.query(State).filter(State.id == data.id).first()
        if not payload_State:
            return {"error_server": "01", "msg": "State not found"}
        
        db_session.delete(payload_State)
        db_session.flush()
        result = {"detail": "State deleted successfully", "data": State_Base(**payload_State.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "delete_State_table_by_id")
        result = {"error_server": "01", "msg": "delete_State_table_by_id: " + str(e)}

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
        query = db_session.query(State)

        if data:
            if data.id:
                query = query.filter(State.id == data.id)
            if data.name:
                query = query.filter(State.name == data.name)
            if data.created_at:
                query = query.filter(State.created_at == data.created_at)
            if data.updated_at:
                query = query.filter(State.updated_at == data.updated_at)

        payload_State = query.all()

        if payload_State:
            result = {
                "detail": "State read successfully",
                "data": [State_Base(**State.__dict__) for State in payload_State]
            }
        else:
            result = {"detail": "State not found", "data": []}
    except Exception as e:
        log_controler.log_error(str(e), "read_State_table_by_condition")
        result = {"error_server": "01", "msg": "read_State_table_by_condition: " + str(e)}

    return result