import os
import json
from settings.configs import HOST, PORT_FASTAPI_DEPARTMENT
from utilitys.http_request import make_request, log_result

# Assuming these are set up as environment variables or constants
if HOST == "xxx.xxx.xxx.xxx":
    BASE_URL = f"http://localhost:{PORT_FASTAPI_DEPARTMENT}/department"
else:
    BASE_URL = f"http://{HOST}:{PORT_FASTAPI_DEPARTMENT}/department"

def test_post_department():
    """Test for post_department."""
    data = {
        "name": "Marketing Department",
        "manager_id": 4
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "post", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("post", "/v1/department/ (post_department)", elapsed_time, error)
    data = response.get("data") if not error else None
    id = data.get("id") if data else None
    return id if not error else None

def test_put_department():
    """Test for put_department."""
    id = test_post_department()
    data = {
        "id": test_post_department,
        "name": "Edit Marketing Department",
        "manager_id": 4
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "put", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("put", "/v1/department/ (put_department)", elapsed_time, error)
    return id if not error else None

def test_get_department_by_condition():
    """Test for get_department_by_condition."""
    id = test_put_department()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "get", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("get", "/v1/department/ (get_department_by_condition)", elapsed_time, error)
    return id if not error else None

def test_delete_department():
    """Test for delete_department."""
    id = test_get_department_by_condition()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "delete", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("delete", "/v1/department/ (delete_department)", elapsed_time, error)
    return response if not error else None

def main_function_test_department():
    """Test all department functions."""
    test_delete_department()