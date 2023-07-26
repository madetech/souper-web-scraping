from unittest.mock import MagicMock

from data.report_reader import get_reports
from fastapi_pagination import LimitOffsetPage
from tests.data.report_fixtures import VALID_REPORTS


def test_get_reports_from_database(mocker):
    mock_session = MagicMock
    mocker.patch('data.report_reader.paginate', return_value= LimitOffsetPage(items=VALID_REPORTS, total=2, limit=2, offset=0))

    reports = get_reports(mock_session)

    assert reports.items == VALID_REPORTS