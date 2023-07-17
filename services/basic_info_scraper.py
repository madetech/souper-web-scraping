# from pprint import pprint
import logging
from bs4 import BeautifulSoup, Tag
import requests
from tabulate import tabulate
from models.basic import Report, Section
import pandas as pd
import numpy as np

#import logging

# needs to be from .env (os.getenv('BASE_URL'))
reports_url = "https://www.gov.uk/service-standard-reports?page="
BASE_URL = "https://www.gov.uk"


def get_report_info(url: str) -> dict:
    info_dict = scrape_report_html(requests.get(url).content)
    return info_dict

def get_all_reports() -> list[Report]:
    report_links = get_all_service_standard_links()
    report_links = report_links[slice(1)]
    reports_models = []
    for link in report_links:
        try:
            report_dict = scrape_report_html(requests.get(f"{BASE_URL}{link}").content)
            reports_models.append(create_report_model(report_dict, link))
        except Exception as e:
            logging.error(f"Failed to scrape report HTML for {link}: {e}")

    return reports_models


def get_all_service_standard_links():
    page_links_count = 0
    page = 1
    total_links = []

    while (page_links_count > 0 or page == 1):
        page_links = get_all_service_standard_links_by_page(page)
        page_links_count = len(page_links)
        total_links.extend(page_links)
        page += 1

    return total_links

def get_all_service_standard_links_by_page(pageNum: int) -> list[str]:
    page = requests.get(f"{reports_url}{pageNum}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = []

    results = soup.find_all("li", {"class": "gem-c-document-list__item"})
    
    for result in results:
        if isinstance(result, Tag):
            link = result.find("a")
            links.append(link["href"])

    return links

def scrape_report_html(content: str) -> dict:
    info_dict = {}
    soup = BeautifulSoup(content, "html.parser")
    results = soup.find("main", id="content")
    info_title_elements = results.find_all("td")

    key_mapping = {
        "Assessment date:": ["Assessment date:"],
        "Result:": ["Result:"],
        "Stage:": ["Stage:", "Assessment stage:"]
    }

    for element in info_title_elements:
        if element.string in ["Assessment date:", "Result:", "Stage:"]:
            for elem in element.next_siblings:
                if elem.name == 'td':
                    key_string = element.string.strip()
                    info_dict[key_string] = elem.get_text().strip()
                    break
    # TODO find report name from page title eg. title_element = results.find_all("h1", {"class":"gem-c-title"})
    return info_dict

def create_report_model(info_dict: dict, url: str) -> Report:
    report = Report()
    report.assessment_date = info_dict["Assessment date:"]
    report.overall_verdict = info_dict["Result:"]
    report.stage = info_dict["Stage:"]
    report.url = url
    report.name = url.split('/')[-1]

    return report