
import requests
import time
from test_oauth2 import get_access_token

# Utility Functions
def make_request(base_url, method, endpoint, data=None, files=None, is_json=True, needs_token=True):
    """
    Makes an HTTP request and returns the response and elapsed time.
    """
    token = get_access_token().get('access_token') if needs_token else None
    headers = {'token': f"Bearer {token}"} if token else {}
    url = f"{base_url}{endpoint}"
    start_time = time.time()
    try:
        if method == "get":
            response = requests.get(url, headers=headers)
        elif method == "post":
            response = requests.post(url, headers=headers, json=data) if is_json else requests.post(url, headers=headers, data=data, files=files)
        elif method == "put":
            response = requests.put(url, headers=headers, json=data) if is_json else requests.put(url, headers=headers, data=data)
        elif method == "delete":
            response = requests.delete(url, headers=headers, json=data)
        else:
            raise ValueError("Invalid HTTP method.")
        response.raise_for_status()
        status_code = response.status_code
        return status_code, response.json(), time.time() - start_time
    except Exception as e:
        return 500, {"error": str(e)}, time.time() - start_time
        
def log_result(operation, endpoint, elapsed_time, error=None):
    """
    Logs the result of an operation.
    """
    status = "FAILED" if error else "PASS"
    error_msg = f" | error: {error}" if error else ""
    print(f"{status} | route: {operation} {endpoint} | elapsed time: {elapsed_time:.2f} seconds{error_msg}")
