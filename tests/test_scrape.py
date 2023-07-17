from models.basic import Report
from services.basic_info_scraper import get_all_reports, get_all_service_standard_links, get_all_service_standard_links_by_page, get_report_info, scrape_report_html, create_report_model
import pytest
import responses
import requests
url = 'https://www.gov.uk/service-standard-reports/get-security-clearance-test'

file = 'tests/data/report_html.txt'

@pytest.fixture
def mocked_report_list_all_response():
    with open('tests/data/report_list_html.txt', 'r') as f:
        report_list = f.read()

    with open('tests/data/report_list_empty_html.txt', 'r') as f:
        report_list_empty = f.read()
    
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url="https://www.gov.uk/service-standard-reports?page=1",
            body=report_list)
        
        rsps.add(
            method=responses.GET,
            url="https://www.gov.uk/service-standard-reports?page=2",
            body=report_list_empty)
        
        yield rsps

@pytest.fixture
def mocked_report_list_page_response():
    with open('tests/data/report_list_html.txt', 'r') as f:
        report_list = f.read()
    
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url="https://www.gov.uk/service-standard-reports?page=1",
            body=report_list)
        
        yield rsps

@pytest.fixture
def mocked_report_response():
    with open('tests/data/report_html.txt', 'r') as f:
        report_content = f.read()

    with responses.RequestsMock() as rsps:
        rsps.get("https://www.gov.uk/service-standard-reports/get-security-clearance-test",
            body=report_content,
            status=200,
            content_type="text/html")
        
        yield rsps

@pytest.fixture
def mocked_main_page_response():
    with open('tests/data/report_list_one.html', 'r') as f:
        page_content = f.read()
    with open('tests/data/report_html.txt', 'r') as f:
        report_content = f.read()
    with open('tests/data/report_list_empty_html.txt', 'r') as f:
        report_list_empty = f.read()

    with responses.RequestsMock() as rsps:
        rsps.add(method=responses.GET,
                url="https://www.gov.uk/service-standard-reports?page=1",
                body=page_content)
        rsps.add(method=responses.GET,
                url="https://www.gov.uk/service-standard-reports/get-security-clearance-test",
                body=report_content)
        rsps.add(
                method=responses.GET,
                url="https://www.gov.uk/service-standard-reports?page=2",
                body=report_list_empty)
        yield rsps

@pytest.fixture
def mocked_main_page_response_one():
    with open('tests/data/report_list_one.html', 'r') as f:
        page_content = f.read()
    with open('tests/data/report_list_empty_html.txt', 'r') as f:
        report_list_empty = f.read()

    with responses.RequestsMock() as rsps:
        rsps.add(method=responses.GET,
                url="https://www.gov.uk/service-standard-reports?page=1",
                body=page_content)
        rsps.add(
            method=responses.GET,
            url="https://www.gov.uk/service-standard-reports?page=2",
            body=report_list_empty)
        
        yield rsps

def test_api(mocked_report_response):
    resp = requests.get("https://www.gov.uk/service-standard-reports/get-security-clearance-test")
    assert resp.status_code == 200

def test_get_report_info_returns_dict(mocked_report_response):
    assert type(get_report_info(url)) == dict
    assert type(get_report_info(url)) != int

def test_report_info_dict_contains_known_keys(mocked_report_response):
    assert get_report_info(url)["Assessment date:"] is not None
    assert get_report_info(url)["Result:"] is not None
    assert get_report_info(url)["Stage:"] is not None

def test_report_info_dict_value_types(mocked_report_response):
    assert type(get_report_info(url)["Assessment date:"]) == str
    assert type(get_report_info(url)["Result:"]) == str
    assert type(get_report_info(url)["Stage:"]) == str

def test_specific_report(mocked_report_response):
    resp = requests.get('https://www.gov.uk/service-standard-reports/get-security-clearance-test')
    assert resp.status_code == 200
    assert get_report_info('https://www.gov.uk/service-standard-reports/get-security-clearance-test')["Assessment date:"] == '23 March 2022'

def test_scrape_report_html_extracts_data():
    with open(file, 'r') as f:
        content = f.read()
    assert scrape_report_html(content)["Assessment date:"] == '23 March 2022'
    assert scrape_report_html(content)["Result:"] == 'Not met'
    assert scrape_report_html(content)["Stage:"] == 'Alpha'

def test_create_report_model():
    info_dict = {
        "Assessment date:": "",
        "Result:": "",
        "Stage:": ""
    }
    assert type(create_report_model(info_dict, url)) == Report

def test_get_all_service_standard_links_by_page_returns_expected_links(mocked_report_list_page_response):
    page_links = get_all_service_standard_links_by_page(1)
    links_per_page = 50
    assert len(page_links) == links_per_page

def test_get_all_service_standard_links_returns_expected_links(mocked_report_list_all_response):
    all_links = get_all_service_standard_links()
    total_link_count = 50
    assert len(all_links) == total_link_count

def test_get_all_service_standard_links_returns_one(mocked_main_page_response_one):
    all_links = get_all_service_standard_links()
    total_link_count = 1
    assert len(all_links) == total_link_count

def test_get_all_reports_returns_list(mocked_main_page_response):
    reports_list = get_all_reports()
    assert type(reports_list) == list