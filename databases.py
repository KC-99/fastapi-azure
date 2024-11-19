import pymysql

# Configure your database connection
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Adance123$",
    "database": "sakila",
    "port": 3306,
}

def get_connection():
    """Creates and returns a new database connection."""
    connection = pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        port=DB_CONFIG["port"],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
