import os
from typing import Iterator

from sqlalchemy import Connection, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session


class souperDB:
    def __init__(self) -> None:
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.database = os.getenv('POSTGRES_DB')

        DATABASE_URL = URL.create(
                    drivername="postgresql",
                    username="postgres",
                    password="password",
                    host="localhost",
                    database="postgres"
                )

        self.engine = create_engine(DATABASE_URL, pool_pre_ping=False)

    def get_engine(self):
        return self.engine

    def get_connection(self):
        return self.engine.connect()