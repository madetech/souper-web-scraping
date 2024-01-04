from collections import namedtuple

DEFAULT_FEEDBACK_COUNT_RESPONSE = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

EXPECTED_FEEDBACK_COUNT_RESPONSE = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [100, 34, 100, 100, 34, 100, 100, 34, 100, 100, 34, 100, 100, 34, 100, 34],
                    [34, 100, 34, 34, 100, 34, 34, 100, 34, 34, 100, 34, 34, 100, 34, 100]]


MockFeedbackResponseResult = namedtuple('MockResult', ["section", "met", "not_met", ])

RESULT_TYPE_FEEDBACK_RESPONSE = [
    MockFeedbackResponseResult(section="1", met=100, not_met= 34),
    MockFeedbackResponseResult(section="2", met =34, not_met= 100),
    MockFeedbackResponseResult(section="3", met= 100, not_met= 34),
    MockFeedbackResponseResult(section="4", met=100, not_met= 34),
    MockFeedbackResponseResult(section="5", met =34, not_met= 100),
    MockFeedbackResponseResult(section="6", met= 100, not_met= 34),
    MockFeedbackResponseResult(section="7", met=100, not_met= 34),
    MockFeedbackResponseResult(section="8", met =34, not_met= 100),
    MockFeedbackResponseResult(section="9", met= 100, not_met= 34),
    MockFeedbackResponseResult(section="10", met=100, not_met= 34),
    MockFeedbackResponseResult(section="11", met =34, not_met= 100),
    MockFeedbackResponseResult(section="12", met= 100, not_met= 34),
    MockFeedbackResponseResult(section="13", met=100, not_met= 34),
    MockFeedbackResponseResult(section="14", met =34, not_met= 100),
    MockFeedbackResponseResult(section="15", met= 100, not_met= 34),
    MockFeedbackResponseResult(section="16", met= 34, not_met= 100)
]
