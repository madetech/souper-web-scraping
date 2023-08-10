from models.feedback import Feedback, FeedbackType

VALID_FEEDBACK = [
    Feedback(
        id=1,
        feedback="some positive feedback",
        type=FeedbackType.POSITIVE
    ),
    Feedback(
        id=2,
        feedback="some constructive feedback",
        type=FeedbackType.CONSTRUCTIVE
    )
]
