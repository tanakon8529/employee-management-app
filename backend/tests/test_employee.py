import os
import json
from settings.configs import HOST, PORT_FASTAPI_EMPLOYEE
from utilitys.http_request import make_request, log_result

# Assuming these are set up as environment variables or constants
if HOST == "xxx.xxx.xxx.xxx":
    BASE_URL = f"http://localhost:{PORT_FASTAPI_EMPLOYEE}/employee"
else:
    BASE_URL = f"http://{HOST}:{PORT_FASTAPI_EMPLOYEE}/employee"

def test_post_employee():
    """Test for post_employee."""
    data = {
        "username": "test",
        "password": "test",
        "name": "testman",
        "position_id": 1,
        "address": "testaddress",
        "manager_id": 1,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Google_Images_2015_logo.svg/640px-Google_Images_2015_logo.svg.png",
        "state_id": 1
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "post", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("post", "/v1/employee/ (post_employee)", elapsed_time, error)
    data = response.get("data") if not error else None
    id = data.get("id") if data else None
    return id if not error else None

def test_put_employee():
    """Test for put_employee."""
    id = test_post_employee()
    data = {
        "id": test_post_employee,
        "name": "edti_testman",
        "position_id": 1,
        "address": "testaddress",
        "manager_id": 1,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Google_Images_2015_logo.svg/640px-Google_Images_2015_logo.svg.png",
        "state_id": 1
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "put", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("put", "/v1/employee/ (put_employee)", elapsed_time, error)
    return id if not error else None

def test_signin_employee():
    """Test for signin_employee."""
    data = {
        "username": "test",
        "password": "test"
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "get", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("get", "/v1/employee/ (signin_employee)", elapsed_time, error)
    return response if not error else None

def test_get_employee_by_condition():
    """Test for get_employee_by_condition."""
    id = test_put_employee()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "get", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("get", "/v1/employee/ (get_employee_by_condition)", elapsed_time, error)
    return id if not error else None

def test_delete_employee():
    """Test for delete_employee."""
    id = test_get_employee_by_condition()
    data = {
        "id": id,
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "delete", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("delete", "/v1/employee/ (delete_employee)", elapsed_time, error)
    return response if not error else None

def main_function_test_employee():
    """Test all employee functions."""
    test_delete_employee()
    test_signin_employee()