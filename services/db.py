from sqlalchemy import create_engine
from sqlalchemy.engine import URL


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="/var/lib/postgresql/data",
    database="data_collector"
)

engine = create_engine(url)

#now connect
connection = engine.connect()