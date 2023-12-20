from sqlalchemy import func
from models.report import Report
from sqlalchemy.orm import Session

# Takes in input from the report table in DB, filters data into sorted arrays based on the stage and number of reports which are used to 
# create React charts for frontend.
def get_result_type_counts(session: Session):
    with session:
            result_set = (
            session.query(Report.stage, Report.overall_verdict, func.count().label('count'))
            .all()
        )
        
    return __format_output(result_set)

def __format_output(result_set):
    sorted_result_set = sorted(
        result_set,
        key=lambda result: (result.stage)
        )

    # referring to the met / not met standards given to each report.
    met = [["Stage", "Count"]]
    not_met = [["Stage", "Count"]]

    for result in sorted_result_set:
        column_detail = [result.stage, result.count]
        if 'MET' == result.overall_verdict.upper():
            met.append(column_detail)
        else:
            not_met.append(column_detail)

    formatted_output = [met, not_met]

    return formatted_output