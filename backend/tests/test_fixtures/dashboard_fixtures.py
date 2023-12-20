from collections import namedtuple


MockResult = namedtuple('MockResult', ['stage', 'overall_verdict', 'count'])
TYPE_COUNT = [
    MockResult(stage='Alpha', overall_verdict='Met', count=20),
    MockResult(stage='Alpha', overall_verdict='Not Met', count=5),
    MockResult(stage='Beta', overall_verdict='Met', count=10),
    MockResult(stage='Beta', overall_verdict='Not Met', count=8),
    MockResult(stage='Live', overall_verdict='Met', count=35),
    MockResult(stage='Live', overall_verdict='Not Met', count=7),
]