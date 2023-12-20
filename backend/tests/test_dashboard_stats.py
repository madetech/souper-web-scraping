import unittest
from unittest.mock import patch
from backend.tests.test_fixtures.dashboard_fixtures import TYPE_COUNT

from backend.data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch('data.dashboard.Session')
    def test_get_counts(self, mock_session):
        mock_session.query.return_value.all.return_value = TYPE_COUNT
        expected = [[["Stage", "Count"],["Alpha", 20],["Beta", 10],["Live", 35]], [["Stage", "Count"],["Alpha", 5],["Beta", 8],["Live", 7]]]
        result = dashboard.get_counts(mock_session)

        self.assertEqual(result, expected)
        