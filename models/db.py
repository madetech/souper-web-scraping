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