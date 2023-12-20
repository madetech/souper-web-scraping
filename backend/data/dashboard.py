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
    sorted_result_set = sorted(
        result_set,
        key=lambda result: (result.stage)
        )

    met = [["Stage", "Count"]]
    not_met = [["Stage", "Count"]]

    for result in sorted_result_set:
        entry = [result.stage, result.count]
        if 'Met' in result:
            met.append(entry)
        else:
            not_met.append(entry)

    formatted_output = [met, not_met]

    return formatted_output