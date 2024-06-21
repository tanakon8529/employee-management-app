import os
import json
from settings.configs import HOST, PORT_FASTAPI_STATE
from utilitys.http_request import make_request, log_result

# Assuming these are set up as environment variables or constants
if HOST == "xxx.xxx.xxx.xxx":
    BASE_URL = f"http://localhost:{PORT_FASTAPI_STATE}/state"
else:
    BASE_URL = f"http://{HOST}:{PORT_FASTAPI_STATE}/state"

def test_post_state():
    """Test for post_state."""
    data = {
        "name": "Suspended",
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "post", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("post", "/v1/state/ (post_state)", elapsed_time, error)
    data = response.get("data") if not error else None
    id = data.get("id") if data else None
    return id if not error else None

def test_put_state():
    """Test for put_state."""
    id = test_post_state()
    data = {
        "id": test_post_state,
        "name": "EDIT Suspended",
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "put", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("put", "/v1/state/ (put_state)", elapsed_time, error)
    return id if not error else None

def test_get_state_by_condition():
    """Test for get_state_by_condition."""
    id = test_put_state()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "get", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("get", "/v1/state/ (get_state_by_condition)", elapsed_time, error)
    return id if not error else None

def test_delete_state():
    """Test for delete_state."""
    id = test_get_state_by_condition()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "delete", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("delete", "/v1/state/ (delete_state)", elapsed_time, error)
    return response if not error else None

def main_function_test_state():
    """Test all state functions."""
    test_delete_state()