from data.database import souperDB
from sqlalchemy import text

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