import logging
from sqlalchemy import func
from models.report import Report
from sqlalchemy.orm import Session

LOGGER = logging.getLogger(__name__)  

# Takes in input from the report table in DB, filters data into sorted arrays based on the stage and number of reports which are used to 
# create React charts for frontend.
def get_result_type_counts(session: Session):
    result_set = None
    try:
        with session:
                result_set = (
                session.query(Report.stage, Report.overall_verdict, func.count().label('count'))
                .group_by(Report.stage, Report.overall_verdict)
                .all()
            )
    except Exception as e:
         LOGGER.error(f"Error '{e}' failed to retrieve counts from DB.")
         
        
    return __format_output(result_set)

def __format_output(result_set):
    sorted_result_set = sorted(
        result_set,
        key=lambda result: (result.stage)
        )
    print(result_set)

    # referring to the met / not met standards given to each report.
    met = [["Stage", "Count"]]
    not_met = [["Stage", "Count"], ["Alpha", 0], ["Beta", 0], ["Live", 0] ]

    for result in sorted_result_set:
        column_detail = [result.stage, result.count]
        if 'MET' == result.overall_verdict.upper():
            met.append(column_detail)
        else:
            for stage in not_met:
                 if stage[0] == result.stage:
                      stage[1] += result.count

    formatted_output = [met, not_met]

    return formatted_output