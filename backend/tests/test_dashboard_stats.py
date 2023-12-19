import unittest
from unittest.mock import patch

from backend.data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch("", return_value='[["alpha", 10, 20], ["beta", 30, 20], ["live", 40, 10]]')
    def test_get_counts(self):
        expected = [["alpha", 10, 20], ["beta", 30, 20], ["live", 40, 10]]
        result = dashboard.getCounts()
        self.assertEqual(result, expected)