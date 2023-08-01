import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


class souperDB:
    def __init__(self) -> None:
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.database = os.getenv('POSTGRES_DB')

        DATABASE_URL = URL.create(
                    drivername="postgresql",
                    username=self.user,
                    password=self.password,
                    host=self.host,
                    database=self.database
                )

        self.engine = create_engine(DATABASE_URL, pool_pre_ping=False)

    def get_engine(self):
        return self.engine
    
    def get_session(self):
        return sessionmaker(self.engine)()

    def get_connection(self):
        return self.engine.connect()