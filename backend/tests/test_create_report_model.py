from models.basic import Report
from tests.fixtures import REPORT_URL
from services.basic_info_scraper import create_report_model

# create_report_model tests
def test_create_report_model():
    info_dict = {
        "assessment_date": "23 March 2022",
        "result": "Not met",
        "stage": "Alpha"
    }
    assert type(create_report_model(info_dict, REPORT_URL)) == Report

def test_create_report_model_with_missing_keys():
    report_dict = {
        "result": "Met"
    }
    report_model = create_report_model(report_dict, REPORT_URL)
    assert report_model.assessment_date == None
    assert report_model.stage == None

def test_create_report_model_with_invalid_date():
    report_dict = {
        "assessment_date": "invalid date",
        "result": "Met",
        "stage": "Alpha"
    }
    assert create_report_model(report_dict, REPORT_URL).assessment_date == None

def test_create_report_model_with_valid_date():
    report_dict = {
        "assessment_date": "23 March 2022"
    }
    assert create_report_model(report_dict, REPORT_URL).assessment_date == "2022-03-23"