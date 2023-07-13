from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from models.basic import Report, Section, Base
from sqlalchemy.orm import Session
import os


def insert_entry(entry: Base, engine):
    with Session(engine) as session:
        session.add(entry)
        session.commit()
    session.close()


class souperDB:
    def __init__(self):
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.database = os.getenv('POSTGRES_DB')
        
        DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
            self.user, self.password, self.host, self.port, self.database
        )
        
        print(DATABASE_URL)
        
        self.engine = create_engine(DATABASE_URL, pool_pre_ping=False)
        
    def get_engine(self):
        return self.engine
    
    def get_connection(self):
        return self.engine.connect()