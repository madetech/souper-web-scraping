from collections import namedtuple

DEFAULT_FEEDBACK_COUNT_RESPONSE = [["Met", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ["Not Met",0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

EXPECTED_FEEDBACK_COUNT_RESPONSE = [["Met", 100, 34, 100, 100, 34, 100, 34, 100, 100, 100, 100, 34, 100, 34, 100, 34],
                                    ["Not Met", 34, 100, 34, 34, 100, 34, 100, 34, 34, 34, 34, 100, 34, 100, 34, 100]]

MockFeedbackResponseResult = namedtuple('MockResult', ["section", "met_count", "not_met_count", ])

RESULT_TYPE_FEEDBACK_RESPONSE = [
    MockFeedbackResponseResult(1, 100, 34),
    MockFeedbackResponseResult(2, 34, 100),
    MockFeedbackResponseResult(3, 100, 34),
    MockFeedbackResponseResult(4, 100, 34),
    MockFeedbackResponseResult(5, 34, 100),
    MockFeedbackResponseResult(6, 100, 34),
    MockFeedbackResponseResult(7, 34, 100),
    MockFeedbackResponseResult(8, 100, 34),
    MockFeedbackResponseResult(9, 100, 34),
    MockFeedbackResponseResult(10, 100, 34),
    MockFeedbackResponseResult(11, 100, 34),
    MockFeedbackResponseResult(12, 34, 100),
    MockFeedbackResponseResult(13, 100, 34),
    MockFeedbackResponseResult(14, 34, 100),
    MockFeedbackResponseResult(15, 100, 34),
    MockFeedbackResponseResult(16, 34, 100)
]
