from sqlalchemy import text
from sqlalchemy import text
from services.db import souperDB

db = souperDB()

def test_dbConnection():
    connection = db.getConnection()
    trans = connection.begin()
    try:
        connection.execute(text('SELECT 1'))
        trans.commit()
        assert True
    except Exception:
        trans.rollback()
        # print('\n\n----------- Connection failed ! ERROR : ', e)
        assert False
