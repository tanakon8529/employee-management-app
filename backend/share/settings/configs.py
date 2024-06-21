
import os
from dotenv import load_dotenv

load_dotenv("./.env")

#### MICROSERVICE ####
MICROSERVICE_NAME_FASTAPI_OAUTH2 = "fastapi-oauth2"
MICROSERVICE_NAME_FASTAPI_EMPLOTYEE = "fastapi-employee"
MICROSERVICE_NAME_FASTAPI_POSITION = "fastapi-position"

def set_microservice_name_by_api_path(api_path):
    if api_path == API_PATH_FASTAPI_OAUTH2:
        return MICROSERVICE_NAME_FASTAPI_OAUTH2
    elif api_path == MICROSERVICE_NAME_FASTAPI_EMPLOTYEE:
        return MICROSERVICE_NAME_FASTAPI_EMPLOTYEE
    elif api_path == MICROSERVICE_NAME_FASTAPI_POSITION:
        return MICROSERVICE_NAME_FASTAPI_POSITION
    else:
        return "Unknown"
    
# APIs
API_VERSION = os.environ["API_VERSION"]
API_DOC = os.environ["API_DOC"]
HOST = os.environ["HOST"]

API_PATH_FASTAPI_OAUTH2 = os.environ["API_PATH_FASTAPI_OAUTH2"]
API_PATH_FASTAPI_EMPLOYEE = os.environ["API_PATH_FASTAPI_EMPLOYEE"]
API_PATH_FASTAPI_POSITION = os.environ["API_PATH_FASTAPI_POSITION"]

PORT_FASTAPI_OAUTH2 = os.environ["PORT_FASTAPI_OAUTH2"]
PORT_FASTAPI_EMPLOYEE = os.environ["PORT_FASTAPI_EMPLOYEE"]
PORT_FASTAPI_POSITION = os.environ["PORT_FASTAPI_POSITION"]

#### AUTHENTICATION ####
USERNAME_ADMIN = os.environ["USERNAME_ADMIN"]
PASSWORD_ADMIN = os.environ["PASSWORD_ADMIN"]
SECRET_KEY = os.environ["SECRET_KEY"] + "="

#### DATABASE SQLITE ####
SQLITE_DB_PATH = os.environ["SQLITE_DB_PATH"]

#### REDIS ####
HOST_REDIS = os.environ["HOST_REDIS"]
PORT_REDIS = os.environ["PORT_REDIS"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]