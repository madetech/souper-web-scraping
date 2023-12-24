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
    formatted_output = [["Stage", "Met", "Not Met"], ["Alpha", 0, 0], ["Beta", 0, 0], ["Live", 0, 0]]

    for result in result_set:
        for section in formatted_output:
            if section[0] == result.stage:
                if 'MET' == result.overall_verdict.upper():
                      section[1] += result.count
                else:
                      section[2] += result.count

    return formatted_output