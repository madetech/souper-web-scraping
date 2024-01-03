from collections import namedtuple

# counts_by_result_type test fixtures
MockCountResult = namedtuple('MockResult', ['stage', 'overall_verdict', 'count'])
RESULT_TYPE_COUNT = [
    MockCountResult(stage='Alpha', overall_verdict='Met', count=20),
    MockCountResult(stage='Alpha', overall_verdict='Not Met', count=5),
    MockCountResult(stage='Beta', overall_verdict='Met', count=10),
    MockCountResult(stage='Beta', overall_verdict='Not Met', count=8),
    MockCountResult(stage='Live', overall_verdict='Met', count=35),
    MockCountResult(stage='Live', overall_verdict='Not Met', count=7),
]

EXPECTED_RESULT_COUNT = [["Stage", "Met", "Not Met"],["Alpha", 20, 5],["Beta", 10, 8],["Live", 35, 7]]

EXPECTED_DEFAULT_COUNT_RESULT = [["Stage", "Met", "Not Met"],["Alpha", 0, 0],["Beta", 0, 0],["Live", 0, 0]]

# average_and_median_by_result_type test fixtures
MockAverageResult = namedtuple('MockResult', ['stage', 'name', 'overall_verdict', 'assessment_date'])
#  the matching mock data for date calculations, are report 1, 2 and 5.
RESULT_TYPE_PERIOD = [
    MockAverageResult(stage='Alpha', name='Report number 1 test name dgdgd', overall_verdict='Not Met', assessment_date='2020-01-10'),
    MockAverageResult(stage='Alpha', name='Report number 1 test name hshs', overall_verdict='Not Met', assessment_date='2020-01-8'),
    MockAverageResult(stage='Alpha', name='Report number 1 test name jete', overall_verdict='Met', assessment_date='2020-01-12'),   
    MockAverageResult(stage='Alpha', name='Report number 2 test name djdjdjd', overall_verdict='Not Met', assessment_date='2020-01-20'),
    MockAverageResult(stage='Alpha', name='Report number 2 test name fhfhf', overall_verdict='Met', assessment_date='2020-01-28'),
    MockAverageResult(stage='Alpha', name='Report number 3 test name jsjs', overall_verdict='Met', assessment_date='2020-01-15'),
    MockAverageResult(stage='Beta', name='Report number 4 test name hfyryur', overall_verdict='Not Met', assessment_date='2020-01-10'),
    MockAverageResult(stage='Beta', name='Report number 5 test name jsjsjs', overall_verdict='Not Met', assessment_date='2020-01-20'),
    MockAverageResult(stage='Beta', name='Report number 5 test name jshsbs', overall_verdict='Met', assessment_date='2020-01-25'),
    MockAverageResult(stage='Live', name='Report number 6 test name shshs', overall_verdict='Met', assessment_date='2020-01-10'),
    MockAverageResult(stage='Live', name='Report number 7 test name jsauasbhdsnds', overall_verdict='Met', assessment_date='2020-01-10'),
]

EXPECTED_RESULT_PERIOD = [["Stage", "Average",  "Median", "Shortest", "Longest"],["Alpha", 6, 6, 4, 8],["Beta", 5, 5, 5, 5],["Live", 0, 0, 0, 0]]

EXPECTED_DEFAULT_PERIOD_RESULT = [["Stage", "Average",  "Median", "Shortest", "Longest" ],["Alpha", 0, 0, 0, 0],["Beta", 0, 0, 0, 0],["Live", 0, 0, 0, 0]]


