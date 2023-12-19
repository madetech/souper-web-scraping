import unittest
from unittest.mock import patch

from data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch("backend.data.session.query", return_value='[]')
    def test_get_counts(self):
        expected = [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        result = dashboard.get_counts(None)
        self.assertEqual(result, expected)
        