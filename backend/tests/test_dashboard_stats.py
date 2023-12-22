import unittest
from unittest.mock import patch
from tests.test_fixtures.chart_fixtures import RESULT_TYPE_COUNT

from backend.data.charts import counts_by_result_type


class DashboardStatsTest(unittest.TestCase):
    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_counts(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = RESULT_TYPE_COUNT
        expected = [[["Stage", "Count"],["Alpha", 20],["Beta", 10],["Live", 35]], [["Stage", "Count"],["Alpha", 5],["Beta", 8],["Live", 7]]]
        result = counts_by_result_type.get_result_type_counts(mock_session)

        self.assertEqual(result, expected)
        