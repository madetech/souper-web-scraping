import unittest
from unittest.mock import patch
from models.report import Report

from backend.data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch('data.dashboard.Session')
    def test_get_counts(self, mock_session):
        query = mock_session.query(Report).filter(Report.stage == 'Alpha')
        mock_session.query.return_value = query
        expected = [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        result = dashboard.get_counts(mock_session)
        self.assertEqual(result, expected)
        