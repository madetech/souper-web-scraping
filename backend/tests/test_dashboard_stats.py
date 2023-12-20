from collections import namedtuple
import unittest
from unittest.mock import Mock, patch
from models.report import Report

from backend.data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch('data.dashboard.Session')
    def test_get_counts(self, mock_session):
        MockRecord = namedtuple('MockRecord', ['stage', 'result', 'count'])
        mock_data = [
            MockRecord(stage='alpha', result='met', count=5),
            MockRecord(stage='alpha', result='not met', count=2),
            MockRecord(stage='beta', result='met', count=15),
            ]
        mock_query = Mock()
        mock_query.filter().count.return_value = 42
        mock_session_instance = mock_session.return_value
        mock_session_instance.query.return_value = mock_query
        expected = [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        result = dashboard.get_counts(mock_session_instance)

        self.assertEqual(result, expected)

        mock_session.assert_called_once_with()
        # mock_session_instance.query.assert_called_once_with(Report)
        # mock_query.filter.assert_called_once_with(Report.stage == "Alpha")
        # mock_query.filter().count.assert_called_once_with()
        