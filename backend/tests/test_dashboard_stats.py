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
    def test_get_result_type_counts_with_no_input(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = []
        result = counts_by_result_type.get_result_type_counts(mock_session)
        expected_result = [["Stage", "Met", "Not Met"],["Alpha", 0, 0],["Beta", 0, 0],["Live", 0, 0]]

        self.assertEqual(result, expected_result)

    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_counts_with_none_input(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = None
        result = counts_by_result_type.get_result_type_counts(mock_session)
        expected_result = [["Stage", "Met", "Not Met"],["Alpha", 0, 0],["Beta", 0, 0],["Live", 0, 0]]

        self.assertEqual(result, expected_result)
    

    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_averages(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = RESULT_TYPE_PERIOD
        result = average_by_result_type.get_result_type_averages(mock_session)

        self.assertEqual(result, EXPECTED_RESULT_PERIOD)


    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_averages_with_no_input(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = []
        expected_result = [["Stage", "Average", "Median"], ["Alpha", 0, 0], ["Beta", 0, 0], ["Live", 0, 0]]
        result = average_by_result_type.get_result_type_averages(mock_session)

        self.assertEqual(result, expected_result)

    @patch('data.charts.counts_by_result_type.Session')
    def test_get_result_type_averages_with_none_input(self, mock_session):
        mock_session.query.return_value.group_by.return_value.all.return_value = None
        expected_result = [["Stage", "Average", "Median"], ["Alpha", 0, 0], ["Beta", 0, 0], ["Live", 0, 0]]
        result = average_by_result_type.get_result_type_averages(mock_session)

        self.assertEqual(result, expected_result)

    def test_get_average_round_down(self):
        input = [4, 5, 6, 6, 7, 8, 7]
        expected_result = 6
        result = average_by_result_type.get_average(input)
        self.assertEqual(result, expected_result)
        
    def test_get_average_round_up(self):
        input = [5, 6, 7, 7, 8, 9]
        expected_result = 7
        result = average_by_result_type.get_average(input)
        self.assertEqual(result, expected_result)
        
        
    def test_get_average_with_input_empty(self):
        input = []
        expected_result = 0
        result = average_by_result_type.get_average(input)
        self.assertEqual(result, expected_result)
    
    def test_get_median_for_even_number_of_values_round_down(self):
        input = [1, 3, 6, 7, 9, 10, 13, 4]
        expected_result = 6
        result = average_by_result_type.get_median(input)
        self.assertEqual(result, expected_result)
    
    def test_get_median_for_even_number_of_values_round_up(self):
        input = [5, 6, 7, 7, 8, 9]
        expected_result = 7
        result = average_by_result_type.get_median(input)
        self.assertEqual(result, expected_result)
    
    def test_get_median_for_odd_number_of_values_round_down(self):
        input = [6, 7, 7, 8, 9]
        expected_result = 7
        result = average_by_result_type.get_median(input)
        self.assertEqual(result, expected_result)
    
    def test_get_median_for_odd_number_of_values_round_up(self):
        input = [6, 6, 7, 7, 8]
        expected_result = 7
        result = average_by_result_type.get_median(input)
        self.assertEqual(result, expected_result)
    
    def test_get_median_with_no_values(self):
        input = []
        expected_result = 0
        result = average_by_result_type.get_median(input)
        self.assertEqual(result, expected_result)
