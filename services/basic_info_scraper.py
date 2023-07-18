# from pprint import pprint
import logging
from bs4 import BeautifulSoup, Tag
import requests
from models.basic import Report, Section

#import logging

# needs to be from .env (os.getenv('BASE_URL'))
reports_url = "https://www.gov.uk/service-standard-reports?page="
BASE_URL = "https://www.gov.uk"


def get_report_info(url: str) -> dict:
    info_dict = scrape_report_html(requests.get(url).content)
    return info_dict

def get_all_reports() -> list[Report]:
    report_links = get_all_service_standard_links()
    #report_links = report_links[slice(1)]
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
    elements = soup.find_all("dt")
    keys_found = set()

    key_mapping = {
        "assessment_date": ["Assessment date:", "Reassessment date:"],
        "result": ["Result", "Result:"],
        "stage": ["Stage", "Stage:", "Assessment stage:"]
    }

    # Loop through each matching element
    for element in elements:
        # Loop through each key in key_mapping
        for key in key_mapping.keys():
            # Check if element text is in list of possible values for the given key
            if element.string.strip() in key_mapping[key]:
                # Store matched key in list
                keys_found.add(key)
                # Get element text and add to dictionary
                value = element.find_next_sibling('dd').get_text().strip()
                info_dict[key] = value
        
        # Exit loop if all keys have been matched
        if len(keys_found) == len(key_mapping.keys()):
            break

    # List keys to retry which have not been matched
    all_keys = set(list(key_mapping.keys()))
    retry_keys = list(all_keys - keys_found)
    
    # Scrape data for missing keys from other elements
    if any(retry_keys):
        # Reset keys found
        keys_found = set()
        elements = soup.find_all("td")
        # Loop through each matching element
        for element in elements:
            # Loop through each key to retry
            for key in retry_keys:
                # Check if element text is in list of possible values for the given key
                if element.string is not None and element.string.strip() in key_mapping[key]:
                    # Store matched key in list
                    keys_found.add(key)
                    # Get element text and add to dictionary
                    value_td = element.find_next_sibling("td")

                    if value_td is not None:
                        info_dict[key] = value_td.get_text()

            # Exit loop if all keys have been matched
            if len(keys_found) == len(key_mapping.keys()):
                break
                    
    # TODO find report name from page title eg. title_element = results.find_all("h1", {"class":"gem-c-title"})
    return info_dict

def create_report_model(info_dict: dict, url: str) -> Report:
    report = Report()
    report.assessment_date = info_dict.get("assessment_date", "")
    report.overall_verdict = info_dict.get("result", "")
    report.stage = info_dict.get("stage", "")
    report.url = url
    report.name = url.split('/')[-1]

    return report