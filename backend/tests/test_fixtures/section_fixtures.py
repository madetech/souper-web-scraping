from models.section import Section

VALID_SECTIONS = [
    Section(
        id=1,
        report_id=1,
        number=1,
        decision="Met",
        feedback=[],
        positive_language_percent = 10,
        constructive_language_percent = 8,
        neutral_language_percent = 4,
        
    ),
    Section(
        id=1,
        report_id=1,
        number=2,
        decision="Not met",
        feedback=[],
        positive_language_percent = 14,
        constructive_language_percent = 3,
        neutral_language_percent = 56,
    )
]
