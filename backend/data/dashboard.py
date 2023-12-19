from models.report import Report
from sqlalchemy.orm import Session


def get_counts(session: Session):
    with session:
        resultSet = session.query(Report).filter(Report.stage == "Alpha").count() # TODO: Fix this to be the correct query: Just pull count of one element first
        print(resultSet)
        results = __format_count_output(resultSet)
    return results

def __format_count_output(resultSet):
    """ Should look like this
    [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        """
    return resultSet