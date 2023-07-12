from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class souperDB:

    DATABASE_URL = URL.create(
        drivername="postgresql",
        username="postgres",
        password="password",
        host="0.0.0.0:5432",
        database="postgres"
    )

    # a method for printing data members
    def getConnection(self):
        self.engine = create_engine(self.DATABASE_URL, pool_pre_ping=True)
        return engine.connect()


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# engine.

# Base = declarative_base()
