from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from core.db_core import Department
from utilities.log_controler import LogControler

log_controler = LogControler()

class Department_Base(BaseModel):
    id: int
    name: Optional[str]
    manager: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

def create_department_table(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Department = Department(
            name=data.name,
            manager_id=data.manager_id
        )
        db_session.add(payload_Department)
        db_session.flush()
        result = {"detail": "Department added successfully", "data": Department_Base(**payload_Department.__dict__)}
    except Exception as e:
        log_controler.log_error(str(e), "fill_department_table")
        result = {"error_server": "01", "msg": "fill_department_table: " + str(e)}

    return result

def update_department_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Department = db_session.query(Department).filter(Department.id == data.id).first()
        payload_Department.name = data.name
        payload_Department.manager_id = data.manager_id
    except Exception as e:
        log_controler.log_error(str(e), "update_department_table_by_id")
        result = {"error_server": "01", "msg": "update_department_table_by_id: " + str(e)}

    return result

def delete_department_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Department = db_session.query(Department).filter(Department.id == data.id).first()
        db_session.delete(payload_Department)
    except Exception as e:
        log_controler.log_error(str(e), "delete_department_table_by_id")
        result = {"error_server": "01", "msg": "delete_department_table_by_id: " + str(e)}

    return result

def read_department_table_by_condition(data, db_session):
    """
        By id
        By name
        By created_at
        By updated_at
    """

    result = {"error_server": "00", "msg": "Server error"}
    try:
        if data.id:
            payload_Department = db_session.query(Department).filter(Department.id == data.id).first()
        elif data.name:
            payload_Department = db_session.query(Department).filter(Department.name == data.name).first()
        elif data.created_at:
            payload_Department = db_session.query(Department).filter(Department.created_at == data.created_at).all()
        elif data.updated_at:
            payload_Department = db_session.query(Department).filter(Department.updated_at == data.updated_at).all()
        else:
            payload_Department = db_session.query(Department).all()

        if payload_Department:
            result = {"detail": "Department read successfully", "data": [Department_Base(**payload_Department.__dict__) for payload_Department in payload_Department]}
        else:
            result = {"detail": "Department not found", "data": []} 
    except Exception as e:
        log_controler.log_error(str(e), "read_department_table_by_condition")
        result = {"error_server": "01", "msg": "read_department_table_by_condition: " + str(e)}

    return result