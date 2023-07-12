from sqlalchemy import text
from services.db import souperDB

def test_dbConnection():
        connection = souperDB.getConnection()
        trans = connection.begin()
        try:
            connection.execute(text('SELECT 1'))
            trans.commit()
            assert True
        except Exception:
            trans.rollback()
            # print('\n\n----------- Connection failed ! ERROR : ', e)
            assert False