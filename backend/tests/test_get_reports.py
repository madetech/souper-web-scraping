from services.basic_info_scraper import scrape_report_html, scrape_reports
from tests.test_fixtures.report_html_fixtures import (
    REPORT_HTML_FILE, mocked_main_page_response)


# get_reports tests
def test_get_reports(mocked_main_page_response):
    report_list = scrape_reports()
    report = report_list[0]
    assert len(report_list) == 1
    assert report.assessment_date == "2022-03-23"
    assert report.overall_verdict == "Not met"
    assert report.stage == "Alpha"

# scrape_report_html tests
def test_scrape_report_html_extracts_data():
    with open(REPORT_HTML_FILE, 'r') as f:
        content = f.read()
    assert scrape_report_html(content)["assessment_date"] == "23 March 2022"
    assert scrape_report_html(content)["result"] == "Not met"
    assert scrape_report_html(content)["stage"] == "Alpha"
