from unittest.mock import MagicMock, patch

from data.report_reader import get_reports
# from fastapi_pagination import LimitOffsetPage
from tests.test_fixtures.report_fixtures import VALID_REPORTS


#@patch('data.report_reader.paginate')
@patch('data.report_reader.Session')
def test_get_reports_from_database(mock_session):
    mock_session.query.return_value.order_by.return_value.all.return_value = VALID_REPORTS

    reports = get_reports(mock_session)

    assert reports == VALID_REPORTS


# def test_get_reports_from_database(mock_session, mock_paginate):
#     mock_paginate.return_value= LimitOffsetPage(items=VALID_REPORTS, total=2, limit=2, offset=0)

#     reports = get_reports(mock_session)

#     assert reports == VALID_REPORTS