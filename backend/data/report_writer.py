import logging

from models.feedback import Feedback
from models.report import Report
from models.section import Section
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

LOGGER = logging.getLogger(__name__)


def upsert_reports(reports: list[Report], session: Session):
    number_of_reports = len(reports)
    LOGGER.info(f"Upserting {number_of_reports} reports")
    index = 1
    for report in reports:
        LOGGER.debug(f"Upserting report {index} of {number_of_reports}")
        report_id = upsert_report(report, session)

        LOGGER.debug("Upserting sections and feedback")
        for section in report.sections:
            section_id = None
            if report_id:
                section_id = upsert_report_section(section, report_id, session)
            if section_id:
                bulk_upsert_feedback(section, section_id, session)

        LOGGER.debug(f"Upsert of report {index} completed")
        index += 1

    session.commit()
    LOGGER.info("Upsert of all records completed")


def upsert_report(report: Report, session: Session):
    report_table = Report.__table__

    # Insert report
    upsert_report_statement = insert(report_table).values( #type: ignore - I think this is legal, VSCode just can't see that FromClause is an instance of Table
        assessment_date=report.assessment_date,
        overall_verdict=report.overall_verdict,
        name=report.name,
        url=report.url,
        stage=report.stage,
        service_provider = report.service_provider
    ).on_conflict_do_update(
        constraint="report_url_key",
        set_=dict(
            service_provider = report.service_provider,
            overall_verdict=report.overall_verdict,
            stage=report.stage,
            assessment_date=report.assessment_date
        )
    ).returning(report_table.c["id"])

    row = session.execute(upsert_report_statement).fetchone()
    if row:
        return row[0]  # report id
    else:
        return None


def upsert_report_section(section: Section, report_id: int, session: Session):
    section_table = Section.__table__

    section_to_insert = dict(
        report_id=report_id,
        number=section.number,
        title=section.title,
        decision=section.decision,
        positive_language_percent=section.positive_language_percent,
        constructive_language_percent = section.constructive_language_percent,
        neutral_language_percent = section.neutral_language_percent
    )

    upsert_section_statement = insert(section_table).values(section_to_insert) #type: ignore - I think this is legal, VSCode just can't see that FromClause is an instance of Table
    upsert_section_statement = upsert_section_statement.on_conflict_do_update(
        constraint="section_report_id_number_key",
        set_=dict(
            decision=upsert_section_statement.excluded.decision,
            title=upsert_section_statement.excluded.title,
        )
    ).returning(section_table.c["id"])

    inserted_section = session.execute(upsert_section_statement).fetchone()
    if inserted_section:
        return inserted_section[0]  # section id
    else:
        return None


def bulk_upsert_feedback(section: Section, section_id: int, session: Session):
    feedback_table = Feedback.__table__

    feedbacks_to_insert = []

    for feedback_item in section.feedback:
        feedbacks_to_insert.append(dict(
            section_id=section_id,
            feedback=feedback_item.feedback,
            type=feedback_item.type
        ))

    if any(feedbacks_to_insert):
        session.execute(insert(feedback_table).values( #type: ignore - I think this is legal, VSCode just can't see that FromClause is an instance of Table
            feedbacks_to_insert).on_conflict_do_nothing())
