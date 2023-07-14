# from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
from tabulate import tabulate
import urllib.parse
from models.basic import Report, Section
import pandas as pd
#import logging

# needs to be from .env (os.getenv('BASE_URL'))
reports_url = "https://www.gov.uk/service-standard-reports?page="
import pytest


def get_report_info(url):
    info_dict = parse_html(requests.get(url).content)
    return info_dict
    #info = {}
    #info["Assessment date:"] = ''
    #info["Result:"] = ''
    #info["Stage:"] = ''
    #return info

def parse_html(content):
    info_dict = {}
    soup = BeautifulSoup(content, "html.parser")
    results = soup.find("main", id="content")
    info_title_elements = results.find_all("dt")
    for element in info_title_elements:
        if element.string in ["Assessment date: ", "Result: ", "Stage: "]:
            for elem in element.next_siblings:
                if elem.name == 'dd':
                    key_string = element.string.strip()
                    info_dict[key_string] = elem.get_text().strip()
                    break
    title_element = results.find_all("h1", {"class":"gem-c-title"})
    # find title

    return info_dict

def create_report_model(info_dict, url):
    report = Report()
    report.assessment_date = info_dict["Assessment date:"]
    report.overall_verdict = info_dict["Result:"]
    report.stage = info_dict["Stage:"]
    report.url = url
    report.name = url.split('/')[-1]