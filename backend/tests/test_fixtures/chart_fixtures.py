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

# average_and_median_by_result_type test fixtures
MockAverageResult = namedtuple('MockResult', ['stage', 'name', 'overall_verdict', 'assessment_date'])
RESULT_TYPE_PERIOD = [
    MockAverageResult(stage='Alpha', name='Rep1', overall_verdict='Not Met', assessment_date='10/01/2020'),
    MockAverageResult(stage='Alpha', name='Rep1', overall_verdict='Met', assessment_date='12/01/2020'),
    MockAverageResult(stage='Alpha', name='Rep2', overall_verdict='Not Met', assessment_date='20/01/2020'),
    MockAverageResult(stage='Alpha', name='Rep2', overall_verdict='Met', assessment_date='14/01/2020'),
    MockAverageResult(stage='Alpha', name='Rep3', overall_verdict='Met', assessment_date='15/02/2020'),
    MockAverageResult(stage='Beta', name='Rep4', overall_verdict='Not Met', assessment_date='10/01/2020'),
    MockAverageResult(stage='Beta', name='Rep5', overall_verdict='Not Met', assessment_date='20/01/2020'),
    MockAverageResult(stage='Beta', name='Rep5', overall_verdict='Met', assessment_date='25/01/2020'),
    MockAverageResult(stage='Live', name='Rep6', overall_verdict='Met', assessment_date='10/02/2020'),
    MockAverageResult(stage='Live', name='Rep7', overall_verdict='Met', assessment_date='10/03/2020'),
]

EXPECTED_RESULT_PERIOD = [["Stage", "Average",  "Median"],["Alpha", 3, 3],["Beta", 5, 5],["Live", 0, 0]]
