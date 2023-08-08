from unittest.mock import patch

from data.feedback_reader import get_feedback
from tests.test_fixtures.feedback_fixtures import VALID_FEEDBACK


@patch('data.feedback_reader.Session')
def test_get_feedback_from_database(mock_session):
    mock_session.query.return_value.filter.return_value.all.return_value = VALID_FEEDBACK

    feedbacks = get_feedback(1, mock_session)

    assert feedbacks == VALID_FEEDBACK
    assert feedbacks.count == VALID_FEEDBACK.count
