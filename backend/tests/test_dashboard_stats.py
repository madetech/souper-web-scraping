import unittest
from unittest.mock import patch

from backend.data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch('data.feedback_reader.Session')
    def test_get_counts(self, mock_session):
        mock_session.query.return_value.filter.return_value.get_counts.return_value = ""
        expected = [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        result = dashboard.get_counts(mock_session)
        self.assertEqual(result, expected)
        