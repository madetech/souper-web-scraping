from models.basic import Report
from services.basic_info_scraper import get_report_info, parse_html

url = ''
file = 'data/report_html.txt'
def test_get_report_info_returns_dict():
    assert type(get_report_info(url)) == dict
    assert type(get_report_info(url)) != int

def test_report_info_dict_contains_known_keys():
    assert get_report_info(url)["Assessment date: "] is not None
    assert get_report_info(url)["Result: "] is not None
    assert get_report_info(url)["Stage: "] is not None

def test_report_info_dict_value_types():
    assert type(get_report_info(url)["Assessment date: "]) == str
    assert type(get_report_info(url)["Result: "]) == str
    assert type(get_report_info(url)["Stage: "]) == str

def test_report_parses():
    with open(file, 'r') as f:
        content = f.read()
    assert parse_html(content)["Assessment date: "] == '23 March 2022'
    assert parse_html(content)["Result: "] == 'Not met'
    assert parse_html(content)["Stage: "] == 'Alpha'
