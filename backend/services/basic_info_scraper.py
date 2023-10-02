import logging

import re
import dateutil.parser as parser
import requests
from bs4 import BeautifulSoup, Tag
from models.feedback import Feedback
from models.report import Report
from models.section import Section
from services.section_info_scraper import scrape_sections_html

LOGGER = logging.getLogger(__name__)

# needs to be from .env (os.getenv('BASE_URL'))
reports_url = "https://www.gov.uk/service-standard-reports?page="
BASE_URL = "https://www.gov.uk"


def scrape_reports() -> list[Report]:
    LOGGER.info("Retrieving report links")
    # report_links = get_report_links()
    # report_links = ["/service-standard-reports/get-security-clearance"]
    # report_links = ["/service-standard-reports/apply-for-legal-aid-alpha-assessment"]
    # report_links = ["/service-standard-reports/business-properties-rental-information-beta-assessment"]
    report_links = ["/service-standard-reports/buy-a-prescription-prepayment-certificate-beta-assessment"]
    reports_models = []
    number_of_reports = len(report_links)
    LOGGER.info(f"Processing {number_of_reports} reports")
    index = 1
    for link in report_links:
        try:
            LOGGER.debug(f"Processing report {index} of {number_of_reports}")
            LOGGER.debug(f"Scraping report")
            report_dict = scrape_report_html(
                requests.get(f"{BASE_URL}{link}").text)
            LOGGER.debug(f"Creating report model")
            reports_models.append(create_report_model(report_dict, link))
        except Exception as e:
            LOGGER.error(
                f"Failed to scrape report HTML for {link}", exc_info=True)

        index += 1

    return reports_models


def get_report_links() -> list[str]:
    page_links_count = 0
    page = 1
    total_links = []

    while (page_links_count > 0 or page == 1):
        LOGGER.debug(f"Retrieving report links for page {page}")
        page_links = get_report_links_by_page(page)
        page_links_count = len(page_links)
        total_links.extend(page_links)
        page += 1

    LOGGER.info(f"Found {len(total_links)} reports to process")
    return total_links


def get_report_links_by_page(pageNum: int) -> list[str]:
    page = requests.get(f"{reports_url}{pageNum}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = []

    results = soup.find_all("li", {"class": "gem-c-document-list__item"})

    for result in results:
        if isinstance(result, Tag):
            element = result.find("a")
            if element and isinstance(element, Tag):
                links.append(element.get("href"))
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

    # This is to cover different report formats and make sure the information is extracted for each type
    scrape_one(soup, key_mapping, report_dict, retry_keys)
    scrape_two(soup, key_mapping, report_dict, retry_keys)
    scrape_three(soup, key_mapping, report_dict, retry_keys)

    # scrape title for each report
    title_element = soup.find("h1")
    if title_element:
        report_dict["name"] = title_element.text.strip()

    # scrape service provider for each report.

    scrape_service_provider(soup, report_dict)
    scrape_service_provider_two(soup, report_dict)

    report_dict["sections"] = scrape_sections_html(soup)
    return report_dict


def scrape_one(soup: BeautifulSoup, key_mapping: dict[str, list[str]], report_dict: dict, retry_keys: list):
    elements = soup.find_all("dt")
    keys_found = set()

    # Loop through each matching element
    # TODO: Refactor loops for each scrape function and pass logic as lambda
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

    elements = soup.select('div.gem-c-govspeak.govuk-govspeak > p strong')

    keys_found = set()
    # Loop through each matching element
    for element in elements:
        # Loop through each key to retry
        for key in retry_keys:
            # Check if element text is in list of possible values for the given key
            if element.string is not None and element.string.lower().strip() in key_mapping[key]:
                # Store matched key in list
                keys_found.add(key)
                # Get element text and add to dictionary. Want to get the element after the next one
                next_element = element.next_sibling
                if next_element:
                    target_element = next_element.next_sibling
                    if target_element:
                        report_dict[key] = target_element.get_text().strip()

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


def scrape_service_provider(soup: BeautifulSoup, report_dict: dict):
    service_provider = soup.find("td", string=re.compile("(?i)(service )?provider(:)?"))
    if service_provider is not None:
        if service_provider.find_next('td'):
            next = service_provider.find_next('td')
            if next:
                text = next.text
                report_dict["service_provider"] = text.strip()

def scrape_service_provider_two(soup: BeautifulSoup, report_dict: dict):
    DEPARTMENT_OR_AGENCY = re.compile(r"(?i)(department) ?/ ?Agency(:)?")
    if service_provider := report_dict.get("service_provider"):
        pass
    else:
        service_provider = soup.find(string=DEPARTMENT_OR_AGENCY)
    
        if service_provider and service_provider.parent and service_provider.parent.parent:
            grandparent = service_provider.parent.parent
            if gp_text := grandparent.get_text():
                report_dict["service_provider"] = DEPARTMENT_OR_AGENCY.sub("", gp_text.replace("\n"," "))


def standardise_verdict_input(info_dict):
    if "result" not in info_dict.keys():
        return "N/A"
    match info_dict["result"]:

        case  "Pass" | "Met" | "Pass with conditions" | "Passed":
            return "Met"
        case "Not Met" | "Not met" | "Not pass" | "Not Pass":
            return "Not met"
        case _:
            return "TBC"


def standardise_stage_input(info_dict):
    if "stage" not in info_dict.keys():
        return "N/A"
    match info_dict["stage"]:

        case "Alpha" | "Alpha2" | "alpha" | "Alpha Review" | "Alpha review" | "Alpha (re-assessment)" | "Alpha - reassessment" | "Alpha reassessment" | "Alpha - reassessment" | "Alpha reassessment":
            return "Alpha"
        case "Beta" | "Beta reassessment" | "Beta2" | "Public Beta" | "Private Beta":
            return "Beta"
        case "Live" | "Live reassessment" | "Live2":
            return "Live"
        case _:
            return "TBC"
        


def create_report_model(report_dict: dict, url: str) -> Report:

    assessment_date = ""
    assessment_date_value = None
    report_name = ""
    service_provider_name = "N/A"

    if "name" in report_dict.keys():
        report_name = report_dict.get("name")
        if not report_name:
            report_name  = ""

    if "service_provider" in report_dict.keys():
        service_provider_name = report_dict.get("service_provider")
        if not service_provider_name:
            service_provider_name = "N/A"

    if "assessment_date" in report_dict.keys():
        assessment_date_value = report_dict.get("assessment_date")

    try:
        if assessment_date_value is not None:
            assessment_date = parser.parse(
                assessment_date_value, default=None, dayfirst=True).date().isoformat()
    except:
        pass

    report = Report()

    report.assessment_date = assessment_date
    report.overall_verdict = standardise_verdict_input(report_dict)
    report.stage = standardise_stage_input(report_dict)
    report.name = report_name
    report.url = url
    report.service_provider = service_provider_name

    if "sections" in report_dict:
        for report_section in report_dict["sections"]:
            section = Section()
            section.number = report_section["number"]
            if "decision" in report_section.keys():
                section.decision = report_section["decision"]
            if "title" in report_section.keys():
                section.title = report_section["title"]
            if "positive_feedback_percentage" in report_section.keys():
                section.positive_language_percent = report_section["positive_feedback_percentage"]
            if "negative_feedback_percentage" in report_section.keys():
                section.constructive_language_percent = report_section["negative_feedback_percentage"]
            if "neutral_feedback_percentage" in report_section.keys():
                section.neutral_language_percent = report_section["neutral_feedback_percentage"]
            

            if "feedback" in report_section:
                for feedback_item in report_section["feedback"]:
                    feedback = Feedback()
                    feedback.feedback = feedback_item[0]
                    feedback.type = feedback_item[1]

                    section.feedback.append(feedback)

            report.sections.append(section)

    return report
