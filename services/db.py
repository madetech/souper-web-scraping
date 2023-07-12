from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class souperDB:



    # a method for printing data members
    def getConnection():
        DATABASE_URL = URL.create(
            drivername="postgresql",
            username="postgres",
            password="password",
            host="/var/lib/postgresql/data",
            database="postgres"
        )
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        return engine.connect()


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# engine.

# Base = declarative_base()
