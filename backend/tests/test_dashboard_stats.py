from collections import namedtuple
import unittest
from unittest.mock import Mock, patch
from models.report import Report

from backend.data import dashboard


class DashboardStatsTest(unittest.TestCase):
    @patch('data.dashboard.Session')
    def test_get_counts(self, mock_session):
        MockResult = namedtuple('MockResult', ['stage', 'overall_verdict', 'count'])
        mock_result_set = [
            MockResult(stage='Alpha', overall_verdict='Met', count=20),
            MockResult(stage='Alpha', overall_verdict='Not Met', count=5),
            MockResult(stage='Beta', overall_verdict='Met', count=10),
            MockResult(stage='Beta', overall_verdict='Not Met', count=8),
            MockResult(stage='Live', overall_verdict='Met', count=35),
            MockResult(stage='Live', overall_verdict='Not Met', count=7),
        ]
        mock_session.query.return_value.all.return_value = mock_result_set
        expected = [[["Stage", "Count"],["Alpha", 20],["Beta", 10],["Live", 35]], [["Stage", "Count"],["Alpha", 5],["Beta", 8],["Live", 7]]]
        result = dashboard.get_counts(mock_session)

        self.assertEqual(result, expected)
        