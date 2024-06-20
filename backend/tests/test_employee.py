import os
import json
from settings.configs import HOST, PORT_FASTAPI_EMPLOYEE
from utilitys.http_request import make_request, log_result

# Assuming these are set up as environment variables or constants
if HOST == "xxx.xxx.xxx.xxx":
    BASE_URL = f"http://localhost:{PORT_FASTAPI_EMPLOYEE}/employee"
else:
    BASE_URL = f"http://{HOST}:{PORT_FASTAPI_EMPLOYEE}/employee"


def test_get_employee_by_condition():
    """Test for get_employee_by_condition."""
    status_code, response, elapsed_time = make_request(BASE_URL, "get", "/v1/")
    error = response.get("detail") if status_code != 200 else None
    log_result("get", "/v1/employee/ (get_employee_by_condition)", elapsed_time, error)
    return response if not error else None

def test_post_employee():
    """Test for post_employee."""
    data = {
        "name": "John Doe",
        "address": "1234 Main St",
        "manager": "Jane Doe",
        "image": "https://example.com/image.jpg"
    }
    status_code, response, elapsed_time = make_request(BASE_URL, "post", "/v1/", data)
    error = response.get("detail") if status_code != 200 else None
    log_result("post", "/v1/employee/ (post_employee)", elapsed_time, error)
    return response if not error else None

def main_function_test_employee():
    """Test all employee functions."""
    test_get_employee_by_condition()
    test_post_employee()