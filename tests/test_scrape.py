from models.basic import Report
from services.basic_info_scraper import get_report_info, parse_html, create_report_model
import pytest
import responses
import requests
url = 'https://www.gov.uk/service-standard-reports/get-security-clearance-test'

file = 'data/report_html.txt'


@pytest.fixture
def mocked_responses():
    with open('data/report_html.txt', 'r') as f:
        content = f.read()
    with responses.RequestsMock() as rsps:
        rsps.get("https://www.gov.uk/service-standard-reports/get-security-clearance-test",
        body=content,
        status=200,
        content_type="text/html")
        yield rsps


def test_api(mocked_responses):
    resp = requests.get("https://www.gov.uk/service-standard-reports/get-security-clearance-test")
    assert resp.status_code == 200


def test_get_report_info_returns_dict(mocked_responses):
    assert type(get_report_info(url)) == dict
    assert type(get_report_info(url)) != int

def test_report_info_dict_contains_known_keys(mocked_responses):
    assert get_report_info(url)["Assessment date:"] is not None
    assert get_report_info(url)["Result:"] is not None
    assert get_report_info(url)["Stage:"] is not None

def test_report_info_dict_value_types(mocked_responses):
    assert type(get_report_info(url)["Assessment date:"]) == str
    assert type(get_report_info(url)["Result:"]) == str
    assert type(get_report_info(url)["Stage:"]) == str

def test_report_parses():
    with open(file, 'r') as f:
        content = f.read()
    assert parse_html(content)["Assessment date:"] == '23 March 2022'
    assert parse_html(content)["Result:"] == 'Not met'
    assert parse_html(content)["Stage:"] == 'Alpha'


def test_specific_report(mocked_responses):
    resp = requests.get('https://www.gov.uk/service-standard-reports/get-security-clearance-test')
    assert resp.status_code == 200
    assert get_report_info('https://www.gov.uk/service-standard-reports/get-security-clearance-test')["Assessment date:"] == '23 March 2022'


def test_create_report_model():
    assert type(create_report_model(url)) == Report