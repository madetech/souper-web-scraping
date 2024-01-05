import logging

from sqlalchemy import case, func
from models.feedback import Feedback
from models.section import Section
from sqlalchemy.orm import Session

LOGGER = logging.getLogger(__name__)  


def get_results_summary_count(session: Session):
    LOGGER.info("get results summary function triggered")
    """ 
    This is the original SQL statement that is implemented below
    SELECT s."number", COUNT(CASE WHEN s.decision = 'Met' THEN f.section_id END) AS met_count, 
    COUNT(CASE WHEN s.decision != 'Met' THEN f.section_id END) AS not_met_count  
    from feedback f join section s on f.section_id = s.id where f."type" = 'CONSTRUCTIVE' 
    group by s."number" order by s."number"
    """
    result_set = None
    try:
        with session:
            result_set = (
                session.query(
                    Section.number,
                    func.count(case((Section.decision == 'Met', Feedback.section_id)).label('met_count')),
                    func.count(case((Section.decision != 'Met', Feedback.section_id)).label('not_met_count'))
                )
                .join(Feedback, Feedback.section_id == Section.id)
                .filter(Feedback.type == 'CONSTRUCTIVE')
                .group_by(Section.number)
                .order_by(Section.number)
                .all()
            )
    except Exception as e:
         LOGGER.error(f"Error '{e}' failed to retrieve feedback counts by section from DB.")
    return __format_output(result_set)

def __format_output(result_set):
    formatted_output = [
                    ["Met", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ["Not Met", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    if result_set == None:
        return formatted_output
    for result in result_set:
            formatted_output[0][int(result[0])] = result[1]
            formatted_output[1][int(result[0])] = result[2]
    # formatted_output[0][0] = 'Met'
    # formatted_output[1][0] = 'Not Met'
                     
    return formatted_output
