from services.basic_info_scraper import get_report_links, get_report_links_by_page
from tests.fixtures import mocked_report_list_all_response, mocked_main_page_response_one, mocked_report_list_page_response

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