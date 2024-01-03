from datetime import datetime
import logging
from models.report import Report
from sqlalchemy.orm import Session

LOGGER = logging.getLogger(__name__)  

# Takes in input from the report table in DB, filters data into sorted arrays based on the stage and number of reports which are used to 
# create React charts for frontend.
def get_result_type_averages(session: Session):
    result_set = None
    try:
        with session:
                result_set = (
                session.query(Report.stage, Report.name, Report.overall_verdict, Report.assessment_date)
                .group_by(Report.stage, Report.name, Report.overall_verdict, Report.assessment_date)
                .all()
            )
    except Exception as e:
         LOGGER.error(f"Error '{e}' failed to retrieve dates from DB.")
         
    return __format_output(result_set)

def __format_output(result_set):
    # This is the format use in the graphs for the frontend, the first array is the names of the columns, the following arrays contain the name for the stage and then the values for the columns
    formatted_output = [["Stage", "Average", "Median"], ["Alpha", 0, 0], ["Beta", 0, 0], ["Live", 0, 0]]

    if result_set == None:
        return formatted_output

    dates = {}

    # Find the most recent date for each set of stage/name/verdict, result set is an array of names tuples, see chart_fixtures.py for example
    for result in result_set:
        composite_key = (result.stage, result.name[:25], result.overall_verdict.upper())
        assessment_date = result.assessment_date

        if composite_key not in dates or assessment_date > dates[composite_key]:
            dates[composite_key] = assessment_date

    elapsed_days_dict = {}

    # Iterate through the data and calculate elapsed days
    for key, date in dates.items():
        # unpack composite key
        stage, name, verdict = key
        current_date = datetime.strptime(date, '%Y-%m-%d')

        # Check if there is a Not Met item to calculate elapsed time from. 'Start date'
        if verdict == 'NOT MET':
        # Check for matching 'Met' event
            met_key = (stage, name, 'MET')
            if met_key in dates:
                met_date = datetime.strptime(dates[met_key], '%Y-%m-%d')
                elapsed_days = (met_date - current_date).days

                if stage not in elapsed_days_dict:
                    elapsed_days_dict[stage] = []
                if elapsed_days > 0:
                    elapsed_days_dict[stage].append(elapsed_days)

    for key, value in elapsed_days_dict.items():
        for item in formatted_output:
            if item[0] == key:
                item[1] = get_average(value)
                item[2] = get_median(value)

    return formatted_output

def get_average(elapsed_days):
     if len(elapsed_days) == 0:
         return 0
     return round(sum(elapsed_days) / len(elapsed_days))
            

def get_median(elapsed_days):
    if len(elapsed_days) == 0:
        return 0
    sorted_list = sorted(elapsed_days)
    list_size = len(sorted_list)
    middle_index = list_size // 2

    if list_size % 2 == 1:
        # For odd number of elements
        median = round(sorted_list[middle_index])
    else:
        # For even number of elements
        median = round((sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2)

    return median
