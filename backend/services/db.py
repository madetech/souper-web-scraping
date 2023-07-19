from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from models.basic import Report, Section, Base

from sqlalchemy.orm import Session
import random
import string


def insert_entry(entry: Base, engine):
    with Session(engine) as session:
        session.add(entry)
        session.commit()
    session.close()


class souperDB:
     
     # a method for printing data members
     def getConnection():

         user = 'postgres'
         password = 'password'
         host = '0.0.0.0'
         port = 5432
         database = 'postgres'

         DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
             user, password, host, port, database
         )

         print(DATABASE_URL)

         engine = create_engine(DATABASE_URL, pool_pre_ping=False)
         return engine.connect()