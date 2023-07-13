# from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
from tabulate import tabulate
import urllib.parse
#from models.basic import Report, Section
import pandas as pd

# needs to be from .env (os.getenv('BASE_URL'))
reports_url = "https://www.gov.uk/service-standard-reports?page="


def get_report_info(url):
    info = {}
    info["Assessment date:"] = ''
    info["Result:"] = ''
    info["Stage:"] = ''
    return info

def parse_html(content):
    info_dict = {}
    soup = BeautifulSoup(content)
    results = soup.find("main", id="content")
    info_title_elements = results.find_all("dt")
    for element in info_title_elements:
        if element.string in ["Assessment date: ", "Result: ", "Stage: "]:
            for elem in element.next_siblings:
                if elem.name == 'dd':
                    key_string = element.string.strip()
                    info_dict[key_string] = elem.get_text().strip()
                    break
    return info_dict
