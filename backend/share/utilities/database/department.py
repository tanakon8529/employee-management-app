from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from core.db_core import Department
from utilities.log_controler import LogControler
from utilities.time_controler import get_current_date

log_controler = LogControler()

class Department_Base(BaseModel):
    id: int
    name: Optional[str]
    manager_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]

def create_department_table(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Department = Department(
            name=data.name,
            manager_id=data.manager_id,
            created_at=get_current_date(),
            updated_at=None
        )
        db_session.add(payload_Department)
        db_session.flush()
        result = {"detail": "Department added successfully", "data": Department_Base(**payload_Department.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "fill_Department_table")
        result = {"error_server": "01", "msg": "fill_Department_table: " + str(e)}

    return result

def update_department_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Department = db_session.query(Department).filter(Department.id == data.id).first()
        if not payload_Department:
            return {"error_server": "01", "msg": "Department not found"}
        
        payload_Department.name = data.name
        payload_Department.manager_id = data.manager_id
        payload_Department.updated_at = get_current_date()
        db_session.flush()
        result = {"detail": "Department updated successfully", "data": Department_Base(**payload_Department.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "update_Department_table_by_id")
        result = {"error_server": "01", "msg": "update_Department_table_by_id: " + str(e)}

    return result

def delete_department_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Department = db_session.query(Department).filter(Department.id == data.id).first()
        if not payload_Department:
            return {"error_server": "01", "msg": "Department not found"}
        
        db_session.delete(payload_Department)
        db_session.flush()
        result = {"detail": "Department deleted successfully", "data": Department_Base(**payload_Department.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "delete_Department_table_by_id")
        result = {"error_server": "01", "msg": "delete_Department_table_by_id: " + str(e)}

    return result

def read_department_table_by_condition(data, db_session):
    """
        By id
        By name
        By manager_id
        By created_at
        By updated_at
    """

    result = {"error_server": "00", "msg": "Server error"}
    try:
        query = db_session.query(Department)

        if data:
            if data.id:
                query = query.filter(Department.id == data.id)
            if data.name:
                query = query.filter(Department.name == data.name)
            if data.manager_id:
                query = query.filter(Department.manager_id == data.manager_id)
            if data.created_at:
                query = query.filter(Department.created_at == data.created_at)
            if data.updated_at:
                query = query.filter(Department.updated_at == data.updated_at)

        payload_Department = query.all()

        if payload_Department:
            result = {
                "detail": "Department read successfully",
                "data": [Department_Base(**Department.__dict__) for Department in payload_Department]
            }
        else:
            result = {"detail": "Department not found", "data": []}
    except Exception as e:
        log_controler.log_error(str(e), "read_Department_table_by_condition")
        result = {"error_server": "01", "msg": "read_Department_table_by_condition: " + str(e)}

    return result