import os

def get_base_url():

    return 'http://store.cincydigitals.com'


def get_database_credentials():

    env = os.environ.get('ENV', 'test')

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    if not db_user or not db_password:
        raise Exception("Environment variables 'DB_USER' and 'DB_PASSWORD' must be set.")

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 8889
    elif env == 'prod':
        db_host = 'demostore.supersqa.com'
        db_port = 3306
    else:
        raise Exception(f"Unknown environment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}

    return db_info
