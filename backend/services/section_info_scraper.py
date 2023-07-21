import re

def get_decision(input) -> str:
    if "not" in input:
        return "Not met"
    else:
        return "Met"


def scrape_sections_html(soup) -> list[dict]:
    section_element_id_dict = {
        "1": "understand-users-and-their-needs",
        "2": "solve-a-whole-problem-for-users",
        "3": "provide-a-joined-up-experience-across-all-channels",
        "4": "make-the-service-simple-to-use",
        "5": "make-sure-everyone-can-use-the-service",
        "6": "have-a-multidisciplinary-team",
        "7": "use-agile-ways-of-working",
        "8": "iterate-and-improve-frequently",
        "9": "create-a-secure-service-which-protects-users-privacy",
        "10": "define-what-success-looks-like-and-publish-performance-data",
        "11": "choose-the-right-tools-and-technology",
        "12": "make-new-source-code-open",
        "13": "use-and-contribute-to-open-standards-common-components-and-patterns",
        "14": "operate-a-reliable-service"
    }

    sections = []

    for element_id in section_element_id_dict:
        section_element = soup.find(["h2", "h3"], id=section_element_id_dict[element_id])
        
        if section_element:
            section_decision = section_element.next_sibling.next_sibling

            sections.append(dict(
                number=int(element_id),
                decision=get_decision(section_decision.text)
            ))

    return sections
