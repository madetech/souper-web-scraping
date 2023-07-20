from services.section_info_scraper import get_decision, scrape_sections_html
from bs4 import BeautifulSoup




def test_scrape_sections_html():
    with open('tests/data/report_html.txt', 'r') as f:
        report_html = f.read()
        soup = BeautifulSoup(report_html, "html.parser")

        sections = scrape_sections_html(soup)
        assert type(sections) == dict
        assert len(sections) == 14

def test_get_decision_with_met_inputs():
    met_input = ["The service met point 1 of the standard"]

    for input in met_input:
        assert get_decision(input) == "Met"

def test_get_decision_with_not_met_inputs():
    not_met_input = ["The service did not meet point 1 of the standard"]

    for input in not_met_input:
        assert get_decision(input) == "Not met"