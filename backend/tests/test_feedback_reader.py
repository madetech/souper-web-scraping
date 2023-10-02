from unittest.mock import patch

from data.feedback_reader import get_feedback
from tests.test_fixtures.feedback_fixtures import VALID_FEEDBACK, Feedback
from sqlalchemy.orm import Query


@patch('data.feedback_reader.Session')
def test_get_feedback_from_database(mock_session):
    mock_session.query.return_value.filter.return_value.all.return_value = VALID_FEEDBACK

    feedbacks = get_feedback(1, mock_session)
    assert feedbacks[0].id == 1
    assert feedbacks[0].feedback == "some positive feedback"

    assert feedbacks == VALID_FEEDBACK
    assert feedbacks.count == VALID_FEEDBACK.count


# Trying to mock part of the 'mock_session.query.return_value.filter.return_value.all.return_value' so that we can test the session ID 
# part, which has no effect if it is mocked to VALID_FEEDBACK

# @patch('data.feedback_reader.Session')
# def test_get_feedback_returns_none_without_id(mock_session):
#     mock_session.query.return_value = None # Not sure what to set this to
#     assert mock_session.query.return_value == None

#     feedbacks = get_feedback(0, mock_session)
#     assert feedbacks[0].id == None