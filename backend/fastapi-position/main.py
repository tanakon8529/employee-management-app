

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from settings.configs import API_VERSION, API_PATH_FASTAPI_POSITION, API_DOC
from endpoint import api_router

from middlewares.middleware_db import DBSessionMiddleware
from utilities.database_connector import sqlite_url
from utilities.log_controler import LogControler
log_controler = LogControler(port=API_PATH_FASTAPI_POSITION)

from core.db_core import init_db
init_db()

app = FastAPI(
    title="FastAPI Position",
    description="FastAPI Position",
    version=API_VERSION,
    docs_url=f"{API_PATH_FASTAPI_POSITION}{API_DOC}",
    redoc_url=None,
    openapi_url=f"{API_PATH_FASTAPI_POSITION}{API_DOC}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=sqlite_url())
app.include_router(api_router, prefix=API_PATH_FASTAPI_POSITION)