from data.database import souperDB
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

db = souperDB()

def test_dbConnection():
    connection = db.get_connection()
    trans = connection.begin()
    try:
        connection.execute(text('SELECT 1'))
        trans.commit()
        assert True
    except Exception:
        trans.rollback()
        # print('\n\n----------- Connection failed ! ERROR : ', e)
        assert False