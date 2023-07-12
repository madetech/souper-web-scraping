from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class souperDB:



    # a method for printing data members
    def getConnection():
        # DATABASE_URL = URL.create(
        #     drivername="postgresql",
        #     username="postgres",
        #     password="password",
        #     host="/var/lib/postgresql/data",
        #     database="postgres"
        # )

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
        return engine.connect() # CANNOT CONNECT


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# engine.

# Base = declarative_base()
