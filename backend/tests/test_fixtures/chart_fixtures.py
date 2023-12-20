from collections import namedtuple

# counts_by_result_type test fixtures
MockResult = namedtuple('MockResult', ['stage', 'overall_verdict', 'count'])
RESULT_TYPE_COUNT = [
    MockResult(stage='Alpha', overall_verdict='Met', count=20),
    MockResult(stage='Alpha', overall_verdict='Not Met', count=5),
    MockResult(stage='Beta', overall_verdict='Met', count=10),
    MockResult(stage='Beta', overall_verdict='Not Met', count=8),
    MockResult(stage='Live', overall_verdict='Met', count=35),
    MockResult(stage='Live', overall_verdict='Not Met', count=7),
]