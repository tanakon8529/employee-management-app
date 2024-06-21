
from __future__ import annotations

from fastapi import HTTPException

from apis.state.submod import get_state_by_condition, post_state, update_state, delete_state_by_id
from utilities.log_controler import LogControler
log_controler = LogControler()

def state_post(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = post_state(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'state_post')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))

def state_get(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = get_state_by_condition(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'state_get')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))

def state_put(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = update_state(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'state_put')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))
        
def state_delete(data, **kwargs):
    try:
        db_session = kwargs.get('db_session')
        result = delete_state_by_id(data, db_session)
        if "error_server" in result or "error_code" in result:
            raise HTTPException(status_code=400, detail='{}'.format(result.get('msg')))
        if isinstance(result, Exception):
            raise HTTPException(status_code=500, detail='{}'.format(result.get('msg')))

        return result
    except Exception as e:
        log_controler.log_error(str(e), 'state_delete')
        if isinstance(e, HTTPException):
            raise
        else:
            raise HTTPException(status_code=500, detail='internal server error: {0}'.format(e))