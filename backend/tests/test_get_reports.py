from services.basic_info_scraper import scrape_report_html, scrape_reports, scrape_two, scrape_one, scrape_three
from tests.test_fixtures.report_html_fixtures import (
    REPORT_HTML_FILE, MISFORMAT_REPORT_HTML_FILE, mocked_main_page_response)
from bs4 import BeautifulSoup

# get_reports tests
def test_get_reports(mocked_main_page_response):
    report_list = scrape_reports()
    report = report_list[0]
    assert len(report_list) == 1
    assert report.assessment_date == "2022-03-23"
    assert report.overall_verdict == "Not met"
    assert report.stage == "Alpha"
    assert report.service_provider == "UK Security Vetting (Cabinet Office)"

# scrape_report_html tests
def test_scrape_report_html_extracts_data():
    with open(REPORT_HTML_FILE, 'r') as f:
        content = f.read()
    assert scrape_report_html(content)["assessment_date"] == "23 March 2022"
    assert scrape_report_html(content)["result"] == "Not met"
    assert scrape_report_html(content)["stage"] == "Alpha"

def test_scrape_two_skips_if_no_retry_keys():
    with open(MISFORMAT_REPORT_HTML_FILE, 'r') as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    report_dict = {}
    retry_keys = []

    key_mapping = {
        "assessment_date": ["assessment date:", "reassessment date:"],
        "stage": ["stage", "stage:", "assessment stage", "assessment stage:", "moving to:"],
        "result": ["result", "result:", "assessment result", "result of assessment:", "result of reassessment", "result of reassessment:"],
    }
    #dict = scrape_two(soup, key_mapping, report_dict, retry_keys)
    #assert dict == ''

    scrape_two(soup, key_mapping, report_dict, retry_keys)
    assert report_dict == {}


def test_scrape_two_with_retry_keys():
    with open(MISFORMAT_REPORT_HTML_FILE, 'r') as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    report_dict = {}
    retry_keys = ["assessment_date", "stage", "result"]

    key_mapping = {
        "assessment_date": ["assessment date:", "reassessment date:"],
        "stage": ["stage", "stage:", "assessment stage", "assessment stage:", "moving to:"],
        "result": ["result", "result:", "assessment result", "result of assessment:", "result of reassessment", "result of reassessment:"],
    }
    #dict = scrape_two(soup, key_mapping, report_dict, retry_keys)
    #assert dict == ''

    scrape_two(soup, key_mapping, report_dict, retry_keys)
    assert report_dict["result"] == 'Pass'