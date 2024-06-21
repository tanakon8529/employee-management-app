import os
import json
from settings.configs import HOST, PORT_FASTAPI_POSITION
from utilitys.http_request import make_request, log_result

# Assuming these are set up as environment variables or constants
if HOST == "xxx.xxx.xxx.xxx":
    BASE_URL = f"http://localhost:{PORT_FASTAPI_POSITION}/position"
else:
    BASE_URL = f"http://{HOST}:{PORT_FASTAPI_POSITION}/position"

def test_post_position():
    """Test for post_position."""
    data = {
        "name": "CTO",
        "details": "Chief Technology Officer"
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "post", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("post", "/v1/position/ (post_position)", elapsed_time, error)
    data = response.get("data") if not error else None
    id = data.get("id") if data else None
    return id if not error else None

def test_put_position():
    """Test for put_position."""
    id = test_post_position()
    data = {
        "id": test_post_position,
        "name": "CTO_edit",
        "details": "Chief Technology Officer"
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "put", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("put", "/v1/position/ (put_position)", elapsed_time, error)
    return id if not error else None

def test_get_position_by_condition():
    """Test for get_position_by_condition."""
    id = test_put_position()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "get", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("get", "/v1/position/ (get_position_by_condition)", elapsed_time, error)
    return id if not error else None

def test_delete_position():
    """Test for delete_position."""
    id = test_get_position_by_condition()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "delete", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("delete", "/v1/position/ (delete_position)", elapsed_time, error)
    return response if not error else None

def main_function_test_position():
    """Test all position functions."""
    test_delete_position()