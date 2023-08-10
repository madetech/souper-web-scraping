import pytest
import responses

REPORT_LIST_URL = "https://www.gov.uk/service-standard-reports"
REPORT_URL = "https://www.gov.uk/service-standard-reports/get-security-clearance-test"
REPORT_HTML_FILE = "tests/test_fixtures/report_html.txt"

@pytest.fixture
def mocked_report_list_all_response():
    with open('tests/test_fixtures/report_list_html.txt', 'r') as f:
        report_list = f.read()

    with open('tests/test_fixtures/report_list_empty_html.txt', 'r') as f:
        report_list_empty = f.read()
    
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url=f"{REPORT_LIST_URL}?page=1",
            body=report_list)
        
        rsps.add(
            method=responses.GET,
            url=f"{REPORT_LIST_URL}?page=2",
            body=report_list_empty)
        
        yield rsps

@pytest.fixture
def mocked_report_list_page_response():
    with open('tests/test_fixtures/report_list_html.txt', 'r') as f:
        report_list = f.read()
    
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url=f"{REPORT_LIST_URL}?page=1",
            body=report_list)
        
        yield rsps

@pytest.fixture
def mocked_report_response():
    with open('tests/test_fixtures/report_html.txt', 'r') as f:
        report_content = f.read()

    with responses.RequestsMock() as rsps:
        rsps.get(REPORT_URL,
            body=report_content,
            status=200,
            content_type="text/html")
        
        yield rsps

@pytest.fixture
def mocked_main_page_response():
    with open('tests/test_fixtures/report_list_one.html', 'r') as f:
        page_content = f.read()
    with open('tests/test_fixtures/report_html.txt', 'r') as f:
        report_content = f.read()
    with open('tests/test_fixtures/report_list_empty_html.txt', 'r') as f:
        report_list_empty = f.read()

    with responses.RequestsMock() as rsps:
        rsps.add(method=responses.GET,
                url=f"{REPORT_LIST_URL}?page=1",
                body=page_content)
        
        rsps.add(method=responses.GET,
                url=REPORT_URL,
                body=report_content)
        rsps.add(
                method=responses.GET,
                url=f"{REPORT_LIST_URL}?page=2",
                body=report_list_empty)
        yield rsps

@pytest.fixture
def mocked_main_page_response_one():
    with open('tests/test_fixtures/report_list_one.html', 'r') as f:
        page_content = f.read()
    with open('tests/test_fixtures/report_list_empty_html.txt', 'r') as f:
        report_list_empty = f.read()

    with responses.RequestsMock() as rsps:
        rsps.add(method=responses.GET,
                url=f"{REPORT_LIST_URL}?page=1",
                body=page_content)
        rsps.add(
            method=responses.GET,
            url=f"{REPORT_LIST_URL}?page=2",
            body=report_list_empty)
        
        yield rsps