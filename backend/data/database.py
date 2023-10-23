import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import logging
LOGGER = logging.getLogger(__name__)

class souperDB:
    def __init__(self) -> None:
        new_dict = {}
        json = os.getenv('SOUPERDB_SECRET')

        if not json:
            raise AttributeError("Environmental variable SOUPERDB_SECRET is not set.")

        
        json = json.replace('"', '').replace('{', '').replace('}', '')
        list = json.split(',')
        for item in list:
            sublist = item.split(':')
            new_dict[sublist[0]] = sublist[1]

        self.user = new_dict["username"]
        self.password = new_dict["password"]
        self.host = new_dict["host"]
        self.port = new_dict["port"]
        self.database = new_dict["dbname"]
        LOGGER.info(f"Connecting to db at {self.host}:{self.port}")
        # self.user = os.getenv('POSTGRES_USER')
        # self.password = os.getenv('POSTGRES_PASSWORD')
        # self.host = os.getenv('POSTGRES_HOST')
        # self.port = os.getenv('POSTGRES_PORT')
        # self.database = os.getenv('POSTGRES_DB')

        DATABASE_URL = URL.create(
                    drivername="postgresql",
                    username=self.user,
                    password=self.password,
                    host=self.host,
                    database=self.database
                )
        LOGGER.info(f"DB URL {DATABASE_URL}")

        self.engine = create_engine(DATABASE_URL, pool_pre_ping=False)
        LOGGER.info(f"Engine: {self.engine}")

    def get_engine(self):
        return self.engine
    
    def get_session(self):
        return sessionmaker(self.engine)()

    def get_connection(self):
        return self.engine.connect()