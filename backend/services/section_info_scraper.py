import re
from bs4 import BeautifulSoup

def get_decision(input) -> str:
    if "not" in input:
        return "Not met"
    else:
        return "Met"


def scrape_sections_html(soup) -> list[dict]:
    sections = []

    scrape_one(soup, sections)

    return sections

def scrape_one(soup: BeautifulSoup, sections: list[dict]):
    section_element_id_dict = {
        "1": ["understand-users-and-their-needs", "understand-user-needs"],
        "2": ["solve-a-whole-problem-for-users", "do-ongoing-user-research"],
        "3": ["provide-a-joined-up-experience-across-all-channels"],
        "4": ["make-the-service-simple-to-use"],
        "5": ["make-sure-everyone-can-use-the-service"],
        "6": ["have-a-multidisciplinary-team"],
        "7": ["use-agile-ways-of-working", "understand-security-and-privacy-issues"],
        "8": ["iterate-and-improve-frequently", "make-all-new-source-code-open"],
        "9": ["create-a-secure-service-which-protects-users-privacy"],
        "10": ["define-what-success-looks-like-and-publish-performance-data", "test-the-end-to-end-service"],
        "11": ["choose-the-right-tools-and-technology"],
        "12": ["make-new-source-code-open", "make-sure-users-succeed-first-time"],
        "13": ["use-and-contribute-to-open-standards-common-components-and-patterns", "make-the-user-experience-consistent-with-govuk"],
        "14": ["operate-a-reliable-service", "encourage-everyone-to-use-the-digital-service"],
        "15": ["collect-performance-data"],
        "16": ["identify-performance-indicators"]
    }

    for section_id in section_element_id_dict.keys():
        element_ids = section_element_id_dict[section_id]

        for index, element_id in enumerate(element_ids):
            section_element = soup.find(["h2", "h3"], id=element_ids[index])
            
            if section_element:
                section_decision = section_element.next_sibling.next_sibling

                sections.append(dict(
                    number=int(section_id),
                    decision=get_decision(section_decision.text)
                ))
                break

def scrape_two(soup: BeautifulSoup, sections: list[dict]):
    return