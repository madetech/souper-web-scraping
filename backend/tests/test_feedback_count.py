import unittest
from unittest.mock import patch
from backend.data.tables import feedback_response_summary
from backend.tests.test_fixtures.feedback_count_fixtures import EXPECTED_FEEDBACK_COUNT_RESPONSE, RESULT_TYPE_FEEDBACK_RESPONSE
from backend.tests.test_fixtures.feedback_count_fixtures import DEFAULT_FEEDBACK_COUNT_RESPONSE


class DashboardStatsTest(unittest.TestCase):
    @patch('data.charts.counts_by_result_type.Session')
    def test_get_feedback_summary_count_with_none_results(self, mock_session):
        mock_session.query.return_value.join.return_value.filter.return_value.group_by.return_value.order_by.return_value.all.return_value = None
        result = feedback_response_summary.get_results_summary_count(mock_session)

        self.assertEqual(result, DEFAULT_FEEDBACK_COUNT_RESPONSE)

    @patch('data.charts.counts_by_result_type.Session')
    def test_get_feedback_summary_count_with__valid_results(self, mock_session):
        mock_session.query.return_value.join.return_value.filter.return_value.group_by.return_value.order_by.return_value.all.return_value = RESULT_TYPE_FEEDBACK_RESPONSE
        result = feedback_response_summary.get_results_summary_count(mock_session)

        self.assertEqual(result, EXPECTED_FEEDBACK_COUNT_RESPONSE )
