# from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
from tabulate import tabulate
import urllib.parse
from models.basic import Report, Section
# had to manually install urllib3==1.26.6
# import plotly.graph_objects as go
reports_url = "https://www.gov.uk/service-standard-reports?page="
# import matplotlib.pyplot as plt
# import plotly.express as px
import pandas as pd


# Assumptions:
# One main page with sub pages, each of which is a report (and the report name is in the last element in the web address)
# Outcomes and section numbers are contained in the sentence following the 'Decision' headings
# There are multiple pages of reports

# class Report():
#     data_dict = {"report": [], "section": []}
#     def __init__(self) -> None:
#         self.name = None
#         self.url = None
#         self.met = None
#         self.section_data = []

# !Needs to be more selective and test for existence
def extract_reports_from_main_page(main_url: str) -> list[Report]:
    report_list = []
    page = requests.get(main_url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("main", id="content")
    url_elements = results.find_all("a")
    for url_element in url_elements:
            url = url_element.get('href')
            if '/service-standard-reports/' in url:
                report = Report()
                report.name = url.split('/')[-1]
                report.url = urllib.parse.urljoin(main_url, url)
                report_list.append(report)
    return report_list

# Gets the job done but probably needs a pairing re-write to be safer and testable
def extract_decisions_from_report(report: Report) -> None:
    #decision_list = []
    section_list = []
    page = requests.get(report.url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("main", id="content")
    decision_elements = results.find_all(["h3", "h2"], id=re.compile("decision"))
    for decision_element in decision_elements:
        section = Section()
        for elem in decision_element.next_siblings: # Could use 'next_sibling'? Assuming the sentence following "Decision" contains the verdict
            if elem.name and elem.name.startswith('h'):
                # stop at next header
                break
            if elem.name == 'p':
                outcome = process_decision(elem.get_text())
                #report.section_data.append(outcome) # For a binary approach, appends a list of 2 elements
                if outcome[1] == 1:
                    #decision_list.append(outcome[0])

                    section.decision = outcome[1]
                section.number = outcome[0]
                #else:
                #    decision_list.append('') # In case we want to add a null character
                #print(elem.get_text(), outcome) # Useful for checking if the 'met/not-met' is correctly matched up to 1/0
                break # Some reports have multiple decisions for a section. Assume the 'met' verdict is the most recent
        section_list.append(section)
    #report.data_dict["report"].append(report.name)
    #report.data_dict["section"].append(decision_list)
    return section_list


def process_decision(decision: str) -> list:
    if not any(char.isdigit() for char in decision): # Doesn't catch all - need a better way to filter the decisions
        section_number = 0
        section_verdict = 0
    else:
        section_number = int(re.findall(r'\d+', decision.split('point')[-1])[0])
        section_verdict = 0 if 'not' in decision else 1
    return [section_number, section_verdict]

def display_results(report: Report) -> None:
    data = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in report.data_dict.items() ]))
    print(tabulate(data, headers='keys', tablefmt='psql'))

def first_pass():
    # !if paging need to look for that button and test is available
    url_list = [reports_url + str(i) for i in range(1, 8)] # Hard-code the number of pages because extracting the number from a page layout is just as
    # use-case-specific but a lot more work
    reports_list = []
    # !Combine for loops
    for url in url_list:
        reports_list.extend(extract_reports_from_main_page(url))
    for report in reports_list:
        extract_decisions_from_report(report)
    display_results(report)
    return report