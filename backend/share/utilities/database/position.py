from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from core.db_core import Position
from utilities.log_controler import LogControler
from utilities.time_controler import get_current_date

log_controler = LogControler()

class Position_Base(BaseModel):
    id: int
    name: Optional[str]
    details: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

def create_position_table(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Position = Position(
            name=data.name,
            details=data.details,
            created_at=get_current_date(),
            updated_at=None
        )
        db_session.add(payload_Position)
        db_session.flush()
        result = {"detail": "Position added successfully", "data": Position_Base(**payload_Position.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "fill_position_table")
        result = {"error_server": "01", "msg": "fill_position_table: " + str(e)}

    return result

def update_position_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Position = db_session.query(Position).filter(Position.id == data.id).first()
        if not payload_Position:
            return {"error_server": "01", "msg": "Position not found"}
        
        payload_Position.name = data.name
        payload_Position.details = data.details
        payload_Position.updated_at = get_current_date()
        db_session.flush()
        result = {"detail": "Position updated successfully", "data": Position_Base(**payload_Position.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "update_position_table_by_id")
        result = {"error_server": "01", "msg": "update_position_table_by_id: " + str(e)}

    return result

def delete_position_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Position = db_session.query(Position).filter(Position.id == data.id).first()
        if not payload_Position:
            return {"error_server": "01", "msg": "Position not found"}
        
        db_session.delete(payload_Position)
        db_session.flush()
        result = {"detail": "Position deleted successfully", "data": Position_Base(**payload_Position.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "delete_position_table_by_id")
        result = {"error_server": "01", "msg": "delete_position_table_by_id: " + str(e)}

    return result

def read_position_table_by_condition(data, db_session):
    """
        By id
        By name
        By created_at
        By updated_at
    """

    result = {"error_server": "00", "msg": "Server error"}
    try:
        query = db_session.query(Position)

        if data:
            if data.id:
                query = query.filter(Position.id == data.id)
            if data.name:
                query = query.filter(Position.name == data.name)
            if data.created_at:
                query = query.filter(Position.created_at == data.created_at)
            if data.updated_at:
                query = query.filter(Position.updated_at == data.updated_at)

        payload_Position = query.all()

        if payload_Position:
            result = {
                "detail": "Position read successfully",
                "data": [Position_Base(**position.__dict__) for position in payload_Position]
            }
        else:
            result = {"detail": "Position not found", "data": []}
    except Exception as e:
        log_controler.log_error(str(e), "read_position_table_by_condition")
        result = {"error_server": "01", "msg": "read_position_table_by_condition: " + str(e)}

    return result