from sqlalchemy import func
from models.report import Report
from sqlalchemy.orm import Session


def get_counts(session: Session):
    with session:
            result_set = (
            session.query(Report.stage, Report.overall_verdict, func.count().label('count'))
            .all()
        )
        
    return __format_count_output(result_set)

def __format_count_output(result_set):
    """ Should look like this
    [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        """
    sorted_result_set = sorted(
        result_set,
        key=lambda result: (result.overall_verdict, result.stage)
        )
    print(sorted_result_set)
    return sorted_result_set