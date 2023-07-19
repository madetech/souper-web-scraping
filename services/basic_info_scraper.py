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

def get_reports() -> list[Report]:
    report_links = get_report_links()
    reports_models = []

    for link in report_links:
        try:
            report_dict = scrape_report_html(requests.get(f"{BASE_URL}{link}").content)
            reports_models.append(create_report_model(report_dict, link))
        except Exception as e:
            logging.error(f"Failed to scrape report HTML for {link}: {e}")

    return reports_models

def get_report_links() -> list[str]:
    page_links_count = 0
    page = 1
    total_links = []

    while (page_links_count > 0 or page == 1):
        page_links = get_report_links_by_page(page)
        page_links_count = len(page_links)
        total_links.extend(page_links)
        page += 1

    return total_links

def get_report_links_by_page(pageNum: int) -> list[str]:
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
    soup = BeautifulSoup(content, "html.parser")
    report_dict = {}
    retry_keys = []

    key_mapping = {
        "assessment_date": ["assessment date:", "reassessment date:"],
        "stage": ["stage", "stage:", "assessment stage", "assessment stage:", "moving to:"],
        "result": ["result", "result:", "assessment result", "result of assessment:", "result of reassessment", "result of reassessment:"],
    }

    scrape_one(soup, key_mapping, report_dict, retry_keys)
    scrape_two(soup, key_mapping, report_dict, retry_keys)
    scrape_three(soup, key_mapping, report_dict, retry_keys)
                    
    # TODO find report name from page title eg. title_element = results.find_all("h1", {"class":"gem-c-title"})
    return report_dict

def scrape_one(soup: BeautifulSoup, key_mapping: dict[str, list[str]], report_dict: dict, retry_keys: list):
    elements = soup.find_all("dt")
    keys_found = set()

    # Loop through each matching element
    for element in elements:
        # Loop through each key in key_mapping
        for key in key_mapping.keys():
            # Check if element text is in list of possible values for the given key
            if element.string.lower().strip() in key_mapping[key]:
                # Store matched key in list
                keys_found.add(key)
                # Get element text and add to dictionary
                value = element.find_next_sibling('dd').get_text().strip()
                report_dict[key] = value
        
        # Exit loop if all keys have been matched
        if len(keys_found) == len(key_mapping.keys()):
            break

    # List keys to retry which have not been matched
    all_keys = set(list(key_mapping.keys()))
    retry_keys[:] = list(all_keys - keys_found)

def scrape_two(soup: BeautifulSoup, key_mapping: dict[str, list[str]], report_dict: dict, retry_keys: list):
    if not any(retry_keys):
        return
    
    content = soup.find("div", { "class": "gem-c-govspeak govuk-govspeak" })
    elements = content.select("p strong")
    keys_found = set()

    # Loop through each matching element
    for element in elements:
        # Loop through each key to retry
        for key in retry_keys:
            # Check if element text is in list of possible values for the given key
            if element.string is not None and element.string.lower().strip() in key_mapping[key]:
                # Store matched key in list
                keys_found.add(key)
                # Get element text and add to dictionary
                value = element.next_sibling.next_sibling
                report_dict[key] = value.get_text().strip()
        
        # Exit loop if all keys have been matched
        if len(keys_found) == len(key_mapping.keys()):
            break

    # List keys to retry which have not been matched
    all_keys = set(list(key_mapping.keys()))
    retry_keys[:] = list(all_keys - keys_found)

def scrape_three(soup: BeautifulSoup, key_mapping: dict[str, list[str]], report_dict: dict, retry_keys: list):
    if not any(retry_keys):
        return

    elements = soup.find_all("td")
    keys_found = set()

    # Loop through each matching element
    for element in elements:
        # Loop through each key to retry
        for key in retry_keys:
            # Check if element text is in list of possible values for the given key
            if element.string is not None and element.string.lower().strip() in key_mapping[key]:
                # Store matched key in list
                keys_found.add(key)
                # Get element text and add to dictionary
                value_td = element.find_next_sibling("td")

                if value_td is not None:
                    report_dict[key] = value_td.get_text()

        # Exit loop if all keys have been matched
        if len(keys_found) == len(key_mapping.keys()):
            break
    
    # List keys to retry which have not been matched
    all_keys = set(list(key_mapping.keys()))
    retry_keys[:] = list(all_keys - keys_found)

def create_report_model(info_dict: dict, url: str) -> Report:
    report = Report()
    report.assessment_date = info_dict.get("assessment_date", "")
    report.overall_verdict = info_dict.get("result", "")
    report.stage = info_dict.get("stage", "")
    report.url = url
    report.name = url.split('/')[-1]

    return report
