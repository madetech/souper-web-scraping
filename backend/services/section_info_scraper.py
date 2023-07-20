import re


def get_decision(input):

    if "not" in input:
        return "Not met"
    else:
        return "Met"


def scrape_sections_html(soup):

    sections_dict = {}

    test = soup.find_all('h3', id = re.compile("decision"))
    for decision_heading in test:
        section_decision_key = decision_heading.find_previous('h2').text.split('.')[0]
        section_decision_value = decision_heading.find_next_sibling('p')

        sections_dict[section_decision_key] = section_decision_value

    return sections_dict
