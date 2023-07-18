# from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
from tabulate import tabulate
import urllib.parse
from models.basic import Report, Section
import pandas as pd

# needs to be from .env (os.getenv('BASE_URL'))
reports_url = "https://www.gov.uk/service-standard-reports?page="
