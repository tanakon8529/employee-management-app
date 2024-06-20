from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from core.db_core import Employee
from utilities.log_controler import LogControler
from utilities.hash_controler import hash_password, verify_password

log_controler = LogControler()

class Employee_Base(BaseModel):
    id: int
    username: str
    password: str
    name: Optional[str]
    position_id: Optional[int]
    address: Optional[str]
    manager_id: Optional[int]
    image: Optional[str]
    state_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]

def replace_password_none(data):
    if type(data) == list:
        for d in data:
            d.password = None
    else:
        data.password = None

    return data

def create_employee_table(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        hashed_password = hash_password(data.Password)

        payload_Employee = Employee(
            username=data.username,
            password=hashed_password,
            name=data.name,
            position_id=data.position_id,
            address=data.address,
            manager_id=data.manager_id,
            image=data.image,
            state_id=data.state_id
        )
        db_session.add(payload_Employee)
        db_session.flush()
        result = {"detail": "Employee added successfully", "data": Employee_Base(**payload_Employee.__dict__)}
        # replace password none, return without password
        result["data"] = replace_password_none(result["data"])
    except Exception as e:
        log_controler.log_error(str(e), "fill_employee_table")
        result = {"error_server": "01", "msg": "fill_employee_table: " + str(e)}

    return result

def update_employee_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Employee = db_session.query(Employee).filter(Employee.id == data.id).first()
        payload_Employee.name = data.name
        payload_Employee.position_id = data.position_id
        payload_Employee.address = data.address
        payload_Employee.manager_id = data.manager_id
        payload_Employee.image = data.image
        payload_Employee.state_id = data.state_id
        db_session.flush()
        result = {"detail": "Employee updated successfully", "data": Employee_Base(**payload_Employee.__dict__)}
        # replace password none, return without password
        result["data"] = replace_password_none(result["data"])
    except Exception as e:
        log_controler.log_error(str(e), "update_employee_table")
        result = {"error_server": "01", "msg": "update_employee_table: " + str(e)}

    return result

def delete_employee_table_by_id(data, db_session):
    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Employee = db_session.query(Employee).filter(Employee.id == data.id).first()
        db_session.delete(payload_Employee)
        db_session.flush()
        result = {"detail": "Employee deleted successfully", "data": Employee_Base(**payload_Employee.__dict__)}
        # replace password none, return without password
        result["data"] = replace_password_none(result["data"])
    except Exception as e:
        log_controler.log_error(str(e), "delete_employee_table")
        result = {"error_server": "01", "msg": "delete_employee_table: " + str(e)}

    return result

def read_employee_table_by_condition(data, db_session):
    """
        By id
        By username
        By name
        By position_id
        By address
        By manager_id
        By state_id
        By created_at
        By updated_at
    """

    result = {"error_server": "00", "msg": "Server error"}
    try:
        query = db_session.query(Employee)

        if data:
            if data.id:
                query = query.filter(Employee.id == data.id)
            if data.username:
                query = query.filter(Employee.username == data.username)
            if data.name:
                query = query.filter(Employee.name == data.name)
            if data.position_id:
                query = query.filter(Employee.position_id == data.position_id)
            if data.address:
                query = query.filter(Employee.address == data.address)
            if data.manager_id:
                query = query.filter(Employee.manager_id == data.manager_id)
            if data.state_id:
                query = query.filter(Employee.state_id == data.state_id)
            if data.created_at:
                query = query.filter(Employee.created_at == data.created_at)
            if data.updated_at:
                query = query.filter(Employee.updated_at == data.updated_at)

        payload_Employee = query.all()
        print(payload_Employee)

        if payload_Employee:
            result = {
                "detail": "Employee read successfully",
                "data": [Employee_Base(**employee.__dict__) for employee in payload_Employee]
            }
            # Replace password with None
            result["data"] = replace_password_none(result["data"])
        else:
            result = {"detail": "Employee not found", "data": []}
    except Exception as e:
        log_controler.log_error(str(e), "read_employee_table_by_condition")
        result = {"error_server": "01", "msg": "read_employee_table_by_condition: " + str(e)}

    return result

def read_signin_by_username_password(data, db_session):
    """
        By username
        By password
    """

    result = {"error_server": "00", "msg": "Server error"}
    try:
        payload_Employee = db_session.query(Employee).filter(Employee.username == data.username).first()
        if payload_Employee:
            if verify_password(data.password, payload_Employee.password):
                result = {"detail": "Signin successfully", "data": Employee_Base(**payload_Employee.__dict__)}
                # replace password none, return without password
                result["data"] = replace_password_none(result["data"])
            else:
                result = {"error_server": "02", "msg": "Signin failed, wrong password"}
        else:
            result = {"error_server": "02", "msg": "Signin failed, wrong username"}
    except Exception as e:
        log_controler.log_error(str(e), "read_signin_by_username_password")
        result = {"error_server": "01", "msg": "read_signin_by_username_password: " + str(e)}

    return result