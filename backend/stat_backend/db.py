import os
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE", "POSTGRESQL")

if DATABASE_ENGINE == "POSTGRESQL":
    DB_URI = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    db_params = {
        "host": os.environ["POSTGRES_HOST"].strip(),
        "database": os.environ["POSTGRES_DB"].strip(),
        "user": os.environ["POSTGRES_USER"].strip(),
        "password": os.environ["POSTGRES_PASSWORD"].strip(),
        "port": os.environ["POSTGRES_PORT"].strip(),
    }
    print(db_params)
    db_config = {
        "SQLALCHEMY_DATABASE_URI": DB_URI.format(**db_params),
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }

elif DATABASE_ENGINE == "SQLITE":
    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    path = dir_path / ".."

    FILE_PATH = f"{path}/db.sqlite3"
    DB_URI = "sqlite+pysqlite:///{file_path}"
    db_config = {
        "SQLALCHEMY_DATABASE_URI": DB_URI.format(file_path=FILE_PATH),
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }

else:
    raise Exception("Incorrent environment var DATABASE_ENGINE")

db = SQLAlchemy()
