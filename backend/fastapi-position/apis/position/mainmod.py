
from __future__ import annotations

from fastapi import HTTPException

from apis.position.submod import get_position_by_condition, post_position, update_position, delete_position_by_id
from utilities.log_controler import LogControler
log_controler = LogControler()

def position_post(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = post_position(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'position_post')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))

def position_get(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = get_position_by_condition(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'position_get')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))

def position_put(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = update_position(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'position_put')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))
        
def position_delete(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = delete_position_by_id(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'position_delete')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))