from models.basic import Report
from services.basic_info_scraper import get_report_info, parse_html #, get_content
import pytest
import responses
import requests
url = 'https://www.gov.uk/service-standard-reports/get-security-clearance-test'
# url = ''
file = 'data/report_html.txt'
#import logging
#LOGGER = logging.getLogger(__name__)

@pytest.fixture
def register_response():
    with open('data/report_html.txt', 'r') as f:
        content = f.read()
    with responses.RequestsMock() as mock:
        mock.add(
            method=responses.GET,
            url="https://www.gov.uk/service-standard-reports/get-security-clearance-test",
            content_type='text/html',
            body=content
        )
    yield mock

def test_get_report_info_returns_dict(register_response):
    assert type(get_report_info(url)) == dict
    assert type(get_report_info(url)) != int

def test_report_info_dict_contains_known_keys(register_response):
    assert get_report_info(url)["Assessment date:"] is not None
    assert get_report_info(url)["Result:"] is not None
    assert get_report_info(url)["Stage:"] is not None

def test_report_info_dict_value_types(register_response):
    assert type(get_report_info(url)["Assessment date:"]) == str
    assert type(get_report_info(url)["Result:"]) == str
    assert type(get_report_info(url)["Stage:"]) == str

def test_report_parses():
    with open(file, 'r') as f:
        content = f.read()
    assert parse_html(content)["Assessment date:"] == '23 March 2022'
    assert parse_html(content)["Result:"] == 'Not met'
    assert parse_html(content)["Stage:"] == 'Alpha'


def test_specific_report(register_response):
    resp = requests.get('https://www.gov.uk/service-standard-reports/get-security-clearance-test')
    assert resp.status_code == 200
   # LOGGER.info("LOG", requests.get(url))
   # assert get_report_info('https://www.gov.uk/service-standard-reports/get-security-clearance-test')["Assessment date:"] == '23 March 2022'


