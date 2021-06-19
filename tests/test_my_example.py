import logging
import pytest
from unittest import mock

import requests
from datasette.my_example import initialize_db, _read_sql, run_aggregate_query

LOGGER = logging.getLogger(__name__)


def test_initialize_db_request_exception() -> None:
    # LOGGER.info("Testing initialize DB")
    with mock.patch("datasette.my_example.requests") as mock_requests:
        # SG: I usually prefer to patch objects using a context manager.
        # The behavior should be pretty much equivalent to the decorator.
        mock_requests.get.side_effect = Exception
        with pytest.raises(Exception):
            initialize_db()
        return


def test_initialize_db_request_success() -> None:
    with mock.patch("datasette.my_example.requests") as mock_requests:
        mock_requests.get("http://test.com")
        mock_requests.return_value.status_code = 200
        assert requests.get("http://test.com").status_code == 200


def test_db_creation_exception() -> None:
    with mock.patch("datasette.my_example.sqlite_utils") as mock_db:
        mock_db.side_effect = Exception
        with pytest.raises(Exception):
            run_aggregate_query()
        return


def test_read_sql() -> None:
    file_content_mock = """Hello World! Hello World is in a file. \
A mocked file. He is not real. But he think he is. \
He doesn't know he is mocked"""
    # place-holder
    fake_file_path = "tests/"
    with mock.patch(
        "builtins.open",
        new=mock.mock_open(read_data=file_content_mock),
        create=True,
    ) as _file:
        actual = _read_sql(fake_file_path)
        _file.assert_called_once()
    print(f"{_file.call_args_list=}")
    expected = file_content_mock
    print(f"{expected=}")
    print(f"{actual=}")
    assert expected == actual
