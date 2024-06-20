import requests
import pytest
import time

from settings.configs import HOST, PORT_FASTAPI_OAUTH2, USERNAME_ADMIN, PASSWORD_ADMIN

# Assuming these are set up as environment variables or constants
if HOST == "xxx.xxx.xxx.xxx":
    BASE_URL = f"http://localhost:{PORT_FASTAPI_OAUTH2}/oauth"
else:
    BASE_URL = f"http://{HOST}:{PORT_FASTAPI_OAUTH2}/oauth"

CLIENT_ID = USERNAME_ADMIN
CLIENT_SECRET = PASSWORD_ADMIN

def get_access_token():
    """Function to obtain an access token."""
    url = f"{BASE_URL}/v1/token/"
    headers = {
        'client-id': CLIENT_ID,
        'client-secret': CLIENT_SECRET,
    }
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()

def test_access_token():
    """Test for obtaining an access token."""
    start_time = time.time()
    try:
        response = get_access_token()
        elapsed_time = time.time() - start_time
        assert response is not None
        print(f"PASS | route: /v1/token | elapsed time: {elapsed_time:.2f} seconds |")
    except Exception as e:
        elapsed_time = time.time() - start_time
        print(f"FAILED | route: /v1/token | elapsed time: {elapsed_time:.2f} seconds | error: {e} |")

@pytest.fixture(scope="module")
def token():
    """Pytest fixture to obtain and return an access token for use in other tests."""
    return get_access_token().get('access_token')

def test_protected_route(token):
    """Test for accessing a protected route."""
    start_time = time.time()
    url = f"{BASE_URL}/v1/protected/"
    headers = {'token': f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        elapsed_time = time.time() - start_time
        print(f"PASS | route: /v1/protected | elapsed time: {elapsed_time:.2f} seconds |")
    except Exception as e:
        elapsed_time = time.time() - start_time
        print(f"FAILED | route: /v1/protected | elapsed time: {elapsed_time:.2f} seconds | error: {e} |")


# Run the tests
if __name__ == "__main__":
    test_access_token()
    token = get_access_token().get('access_token')
    test_protected_route(token)
