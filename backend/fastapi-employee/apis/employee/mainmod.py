
from __future__ import annotations

from fastapi import HTTPException

from apis.employee.submod import get_employee_by_condition, post_employee, update_employee, delete_employee_by_id, signin_employee_by_username_password
from utilities.log_controler import LogControler
log_controler = LogControler()

def employee_post(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = post_employee(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'employee_post')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))

def employee_get(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        if kwargs.get('signin'):
            if not data.username or not data.password:
                raise HTTPException(status_code=400, detail='username and password must be filled')
            
            result = signin_employee_by_username_password(data, db_session)
        else:
            result = get_employee_by_condition(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'employee_get')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))

def employee_put(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = update_employee(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'employee_put')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))
        
def employee_delete(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = delete_employee_by_id(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'employee_delete')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))