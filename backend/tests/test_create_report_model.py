from models.report import Report
from services.basic_info_scraper import create_report_model
from tests.test_fixtures.report_html_fixtures import REPORT_URL


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
    assert create_report_model(report_dict, REPORT_URL).assessment_date == "2022-03-23"
