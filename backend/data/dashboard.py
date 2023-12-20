from sqlalchemy import func
from models.report import Report
from sqlalchemy.orm import Session


def get_counts(session: Session):
    with session:
            result_set = (
            session.query(Report.stage, Report.overall_verdict, func.count().label('count'))
            .group_by(Report.stage, Report.overall_verdict)
            .all()
        )
        
    # for result in result_set:
    #     print(f"Stage: {result.stage}, Type: {result.overall_verdict}, Count: {result.count}")
    return result_set

def __format_count_output(resultSet):
    """ Should look like this
    [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        """
    return resultSet