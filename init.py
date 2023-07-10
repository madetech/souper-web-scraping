from sqlalchemy.ext.declarative import declarative_base
from models import basic
from sqlalchemy import create_engine

path="postgresql://postgres:password@localhost/test"
engine = create_engine(path, echo=True)
basic.metadata.create_all(engine)