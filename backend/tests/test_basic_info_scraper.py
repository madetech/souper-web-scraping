from models.report import Report
from services.basic_info_scraper import create_report_model, get_report_links, get_report_links_by_page, scrape_report_html, scrape_reports, scrape_two
from tests.test_fixtures.report_html_fixtures import (
    mocked_main_page_response_one, mocked_report_list_all_response,
    mocked_report_list_page_response, REPORT_HTML_FILE, MISFORMAT_REPORT_HTML_FILE, REPORT_URL, mocked_main_page_response)
from bs4 import BeautifulSoup

# create_report_model tests
def test_create_report_model():
    report_dict = {
        "assessment_date": "23 March 2022",
        "result": "Not met",
        "stage": "Alpha",
        "name": "get security clearance",
        "service_provider": "HMRC"
    }
    assert type(create_report_model(report_dict, REPORT_URL)) == Report

def test_create_report_model_with_missing_keys():
    report_dict = {
        "result": "Met",
        "service_provider": "N/A"
    }
    report_model = create_report_model(report_dict, REPORT_URL)
    assert report_model.assessment_date == ""
    assert report_model.stage == "N/A"
    assert report_model.name == ""

def test_create_report_model_with_invalid_date():
    report_dict = {
        "assessment_date": "invalid date",
        "result": "Met",
        "stage": "Alpha",
        "name": "get security clearance",
        "service_provider": "HMRC"
    }
    assert create_report_model(report_dict, REPORT_URL).assessment_date == ""

def test_create_report_model_with_valid_date():
    report_dict = {
        "assessment_date": "23 March 2022"
    }
    report_model = create_report_model(report_dict, REPORT_URL)
    assert report_model.assessment_date == "2022-03-23"
    assert report_model.service_provider == "N/A"
    assert report_model.name == ""

def test_create_report_model_varying_terms():
    report_dict = {
        "assessment_date": "invalid date",
        "result": "Pass",
        "stage": "Alpha2",
        "name": "get security clearance",
        "service_provider": "HMRC"
    }
    report_model = create_report_model(report_dict, REPORT_URL)
    assert report_model.overall_verdict == "Met"
    assert report_model.stage == "Alpha"

def test_creat_report_model_sections():
    report_dict = {
        "assessment_date": "invalid date",
        "result": "Met",
        "stage": "Alpha",
        "name": "get security clearance",
        "service_provider": "HMRC",
        "sections": [{"number": 16, 
                     "decision": "Met", 
                     "title": "Test", 
                     "positive_feedback_percentage": 100, 
                     "negative_feedback_percentage": 0,
                     "neutral_feedback_percentage": 0}]
    }
    report_model = create_report_model(report_dict, REPORT_URL)
    assert report_model.sections[0].decision == "Met"
    assert report_model.sections[0].number == 16

def test_creat_report_model_feedback():
    report_dict = {
        "assessment_date": "invalid date",
        "result": "Met",
        "stage": "Alpha",
        "name": "get security clearance",
        "service_provider": "HMRC",
        "sections": [{"feedback": [("This is some test feedback", "positive")], 
                     "decision": "Met"}]
    }
    report_model = create_report_model(report_dict, REPORT_URL)
    assert type(report_model) == Report
    assert report_model.sections[0].decision == "Met"
    assert report_model.sections[0].feedback[0].type == "positive"
    assert len(report_model.sections) == 1
    

# get_report_links tests
def test_get_report_links_returns_expected_links(mocked_report_list_all_response):
    all_links = get_report_links()
    total_link_count = 50
    assert len(all_links) == total_link_count

def test_get_report_links_returns_one(mocked_main_page_response_one):
    all_links = get_report_links()
    total_link_count = 1
    assert len(all_links) == total_link_count

# get_report_links_by_page tests
def test_get_report_links_by_page_returns_expected_links(mocked_report_list_page_response):
    page_links = get_report_links_by_page(1)
    links_per_page = 50
    assert len(page_links) == links_per_page
    assert page_links[1] == "/service-standard-reports/declare-your-business-trade-and-cost-information-alpha-assessment-report"


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
    scrape_two(soup, key_mapping, report_dict, retry_keys)
    assert report_dict["result"] == 'Pass'

# def test_scrape_one_with_retry_keys():
#     with open(REPORT_HTML_FILE, 'r') as f:
#         content = f.read()
#     soup = BeautifulSoup(content, "html.parser")
#     report_dict = {}
#     retry_keys = ["assessment_date", "stage", "result"]
#     key_mapping = {
#         "assessment_date": ["assessment date:", "reassessment date:"],
#         "stage": ["stage", "stage:", "assessment stage", "assessment stage:", "moving to:"],
#         "result": ["result", "result:", "assessment result", "result of assessment:", "result of reassessment", "result of reassessment:"],
#     }
#     scrape_one(soup, key_mapping, report_dict, retry_keys)
#     assert report_dict["result"] == 'Not met'