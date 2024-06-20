
import os
from dotenv import load_dotenv

load_dotenv("../.env")

# APIs
HOST = os.environ["HOST"]
PORT_FASTAPI_OAUTH2 = os.environ["PORT_FASTAPI_OAUTH2"]
PORT_FASTAPI_EMPLOYEE = os.environ["PORT_FASTAPI_EMPLOYEE"]

#### AUTHENTICATION ####
USERNAME_ADMIN = os.environ["USERNAME_ADMIN"]
PASSWORD_ADMIN = os.environ["PASSWORD_ADMIN"]