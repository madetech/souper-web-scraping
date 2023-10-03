from bs4 import BeautifulSoup, PageElement, NavigableString
from models.feedback import FeedbackType
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_decision(input: str) -> str:
    lower_case_input = input.lower()
    if any(map(lower_case_input.__contains__, ["not met", "not pass", "not meet"])):
        return "Not met"
    if any(map(lower_case_input.__contains__, ["met", "pass", "passed"])):
        return "Met"
    if "tbc" in lower_case_input:
        return "TBC"
    
    return "N/A"

def scrape_sections_html(soup) -> list[dict]:
    sections = []

    scrape_one(soup, sections)
    scrape_two(soup, sections)

    return sections

section_element_id_dict = {
    "1": ["understand-users-and-their-needs", "understand-user-needs"],
    "2": ["solve-a-whole-problem-for-users", "do-ongoing-user-research"],
    "3": ["provide-a-joined-up-experience-across-all-channels", "have-a-multidisciplinary-team"],
    "4": ["make-the-service-simple-to-use", "use-agile-methods"],
    "5": ["make-sure-everyone-can-use-the-service", "iterate-and-improve-frequently"],
    "6": ["have-a-multidisciplinary-team"],
    "7": ["use-agile-ways-of-working", "understand-security-and-privacy-issues"],
    "8": ["iterate-and-improve-frequently", "make-all-new-source-code-open"],
    "9": ["create-a-secure-service-which-protects-users-privacy", "create-a-secure-service-that-protects-users-privacy", "use-open-standards-and-common-platforms"],
    "10": ["define-what-success-looks-like-and-publish-performance-data", "test-the-end-to-end-service"],
    "11": ["choose-the-right-tools-and-technology"],
    "12": ["make-new-source-code-open", "make-sure-users-succeed-first-time"],
    "13": ["use-and-contribute-to-open-standards-common-components-and-patterns", "make-the-user-experience-consistent-with-govuk"],
    "14": ["operate-a-reliable-service", "encourage-everyone-to-use-the-digital-service"],
    "15": ["collect-performance-data"],
    "16": ["identify-performance-indicators"]
}


def analyse_feedback(feedback_string):
    analysed_percentages =[]
    si_obj = SentimentIntensityAnalyzer()
    sentiment_dict = si_obj.polarity_scores(feedback_string)
    analysed_percentages.insert(0,sentiment_dict['neg']*100)
    analysed_percentages.insert(0,sentiment_dict['neu']*100)
    analysed_percentages.insert(0,sentiment_dict['pos']*100)

    return analysed_percentages

def extract_text_from_feedback(feedback):
    feedback_concat = []
    feedback_string = ' '
    for text in feedback:
        feedback_concat.insert(0,text[0])
    return feedback_string.join(feedback_concat)




def scrape_one(soup: BeautifulSoup, sections: list[dict]):

    for section_id in section_element_id_dict.keys():
        element_ids = section_element_id_dict[section_id]

        for index, _ in enumerate(element_ids):
            section_element = soup.find(["h2", "h3"], id=element_ids[index])

            if not section_element:
                continue

            decision_heading = section_element.find_next_sibling(lambda tag: "Decision" in tag.text) # type: ignore

            if not decision_heading:
                continue

            section_decision = decision_heading.find_next_sibling()

            if not section_decision:
                break

            feedback = []
            feedback.extend(extract_feedback(section_decision, "what-the-team-has-done-well", FeedbackType.POSITIVE))
            feedback.extend(extract_feedback(section_decision, "what-the-team-needs-to-explore", FeedbackType.CONSTRUCTIVE))
            feedback_text = extract_text_from_feedback(feedback)
            analysed_feedback = analyse_feedback(feedback_text)
            

            sections.append(dict(
                number=int(section_id),
                decision=get_decision(section_decision.text),
                title = section_element.text.strip(),
                feedback = feedback,
                positive_feedback_percentage = analysed_feedback[0],
                neutral_feedback_percentage = analysed_feedback[1],
                negative_feedback_percentage = analysed_feedback[2],
            ))
            break

def extract_feedback(element: PageElement, partial_id: str, feedback_type: FeedbackType) -> list[tuple[str,FeedbackType]]:
    feedback = []
    heading = element.find_next_sibling("h3", id=strain_by_partial_id(partial_id))
            
    if heading:
        feedback_chunk = heading.find_next_sibling("ul")

        if feedback_chunk:
            for list_item in feedback_chunk:
                if list_item.text != "\n": # type: ignore
                    feedback.append((list_item.text.strip(), feedback_type)) # type: ignore
    
    return feedback

def strain_by_partial_id(id: str):
    return lambda x: x and x.startswith(id)

def scrape_two(soup: BeautifulSoup, sections: list[dict]):
    if any(sections):
        return
    
    feedback = []
    feedback_title = soup.find("h2",id="the-service-met-the-standard-because")
    if feedback_title:
        feedback_chunk = feedback_title.find_next_sibling("ul")
        if feedback_chunk:
            for list_item in feedback_chunk:
                if list_item.text != "\n": #type: ignore
                    feedback.append((list_item.text.strip(), FeedbackType.POSITIVE)) # type: ignore
    sections.append(dict(
        number = 0,
        title = feedback_title,
        feedback = feedback

    ))


    heading = soup.find("h2", id="digital-service-standard-points")

    if not heading:
        return

    table = heading.find_next_sibling("table")

    if not table:
        return
    rows = []
    if not isinstance(table, NavigableString):
        rows = table.find_all("tr") # type: ignore

    for index, row in enumerate(rows):
        if index == 0:
            continue
        cells = row.find_all("td")
        offset = 0
        if cells[0].text=='\u2028' or cells[0].text=='\xa0':
            offset = 1

        sections.append(dict(
            number=int(cells[0 + offset].text),
            title=cells[1 + offset].text.strip(),
            decision=get_decision(cells[2 + offset].text)
        ))