
def test_scrape_sections_html():
    sections = scrape_sections_html(soup)
    assert type(sections) == list[dict]
    assert len(sections) == 14

def test_get_decision_with_met_inputs():
    met_input = ["The service did not meet point 1 of the standard"]

    for input in met_input:
        assert get_decision(met_input) == "met"

def test_get_decision_with_not_met_inputs():
    not_met_input = "The service met point 1 of the standard"

    for input in not_met_input:
        assert get_decision(not_met_input) == "not met"