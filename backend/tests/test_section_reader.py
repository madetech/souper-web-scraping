from unittest.mock import patch

from data.section_reader import get_sections
from tests.data.section_fixtures import VALID_SECTIONS


@patch('data.section_reader.Session')
def test_get_sections_from_database(mock_session):
    mock_session.query.return_value.filter.return_value.all.return_value = VALID_SECTIONS
 
    sections = get_sections(1, mock_session)

    assert sections == VALID_SECTIONS
    assert sections.count == VALID_SECTIONS.count