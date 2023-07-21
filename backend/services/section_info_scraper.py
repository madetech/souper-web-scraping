import re

def get_decision(input) -> str:
    if "not" in input:
        return "Not met"
    else:
        return "Met"


def scrape_sections_html(soup) -> list[dict]:
    sections = []
    test = soup.find_all('h3', id = re.compile("decision"))

    for decision_heading in test:
        section_number_text = decision_heading.find_previous('h2').text.split('.')[0]
        section_decision = decision_heading.find_next_sibling('p')

        try:
            section_number = int(section_number_text)
        except:
            section_number = None

        existing_sections = list(filter(lambda sections: sections["number"] == section_number, sections))

        if section_number != None or any(existing_sections):
            sections.append(dict(
                number=section_number,
                decision=get_decision(section_decision.text)
            ))

    return sections
