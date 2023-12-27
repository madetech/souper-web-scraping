from datetime import datetime
import logging
from sqlalchemy import func
from models.report import Report
from sqlalchemy.orm import Session
from collections import defaultdict

LOGGER = logging.getLogger(__name__)  

# Takes in input from the report table in DB, filters data into sorted arrays based on the stage and number of reports which are used to 
# create React charts for frontend.
def get_result_type_averages(session: Session):
    result_set = None
    try:
        with session:
                result_set = (
                session.query(Report.stage, Report.name, Report.overall_verdict, Report.assessment_date)
                .group_by(Report.stage, Report.name, Report.overall_verdict)
                .all()
            )
    except Exception as e:
         LOGGER.error(f"Error '{e}' failed to retrieve counts from DB.")
         
    return __format_output(result_set)

# TODO: Try and clean this function up. It is convoluted and horrible
# Questions around date availability. How do we calculqate if there is a Met but no Not Met?
def __format_output(result_set):

    formatted_output = [["Stage", "Average", "Median"], ["Alpha", 0, 0], ["Beta", 0, 0], ["Live", 0, 0]]

    dates = {}

    # Find the most recent date for each set of stage/name/verdict
    for result in result_set:
        key = (result.stage, result.name, result.overall_verdict)
        current_date = result.assessment_date

        if key not in dates or current_date > dates[key]:
            dates[key] = current_date

    elapsed_days_dict = {}

    # Iterate through the data and calculate elapsed days
    for key, date in dates.items():
        stage, name, verdict = key
        current_date = datetime.strptime(date, '%d/%m/%Y')

        # Check if there is a Not Met item to calculate elapsed time from
        if verdict == 'Not Met':
        # Check for matching 'Met' event
            met_key = (stage, name, 'Met')
            if met_key in dates:
                met_date = datetime.strptime(dates[met_key], '%d/%m/%Y')
                elapsed_days = (met_date - current_date).days

                if stage not in elapsed_days_dict:
                    elapsed_days_dict[stage] = []
                elapsed_days_dict[stage].append(elapsed_days)

    for key, value in elapsed_days_dict.items():
        for item in formatted_output:
            if item[0] == key:
                item[1] = get_average(value)
                item[2] = get_median(value)

    return formatted_output

def get_average(elapsed_days):
     return round(sum(elapsed_days) / len(elapsed_days))
            

def get_median(elapsed_days):
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
