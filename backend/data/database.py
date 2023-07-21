from typing import Iterator

from sqlalchemy import Connection, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

DATABASE_URL = URL.create(
            drivername="postgresql",
            username="postgres",
            password="password",
            host="localhost",
            database="postgres"
        )

engine = create_engine(DATABASE_URL, pool_pre_ping=False)

def get_database() -> Iterator[Session]:
    with Session(engine) as database, database.begin():
        yield database

class souperDB:
    # a method for printing data members
    def getConnection(self) -> Connection:
        return engine.connect()