import unittest
from unittest.mock import patch
from tests.test_fixtures.chart_fixtures import EXPECTED_RESULT_COUNT, EXPECTED_RESULT_PERIOD, RESULT_TYPE_COUNT, RESULT_TYPE_PERIOD

from backend.data.charts import average_by_result_type, counts_by_result_type


class DashboardStatsTest(unittest.TestCase):
    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_counts(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = RESULT_TYPE_COUNT
        result = counts_by_result_type.get_result_type_counts(mock_session)

        self.assertEqual(result, EXPECTED_RESULT_COUNT)

    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_averages(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = RESULT_TYPE_PERIOD
        result = average_by_result_type.get_result_type_averages(mock_session)

        self.assertEqual(result, EXPECTED_RESULT_PERIOD)
        