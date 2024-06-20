
from settings.configs import SQLITE_DB_PATH

def sqlite_url():
    # Path to your SQLite database file inside the Docker container
    sqlite_db_path = SQLITE_DB_PATH
        
    # Create a SQLite connection URL
    sqlite_url = f"sqlite:///{sqlite_db_path}"
    return sqlite_url