import logging
import pytest
from unittest import mock
from datasette.my_example import initialize_db

LOGGER = logging.getLogger(__name__)


def test_initialize_db_exception() -> None:
    # LOGGER.info("Testing initialize DB")
    with mock.patch("datasette.my_example.requests") as mock_requests:
        # SG: I usually prefer to patch objects using a context manager.
        # The behavior should be pretty much equivalent to the decorator.
        mock_requests.get.side_effect = Exception
        with pytest.raises(Exception):
            initialize_db()

            # mock_requests.get.assert_called_once() This row is not needed
            # as it throws exception a the prev line
        return


# def test_read_sql() -> None:
#     file_content_mock = """Hello World! Hello World is in a file. \
# A mocked file. He is not real. But he think he is. \
# He doesn't know he is mocked"""
#     fake_file_path = "tests/"
#     with mock.patch(
#         "datasette.my_example._read_sql.open",
#         new=mock.mock_open(read_data=file_content_mock),
#         create=True,
#     ) as _file:
#         actual = _read_sql(fake_file_path)
#         _file.assert_called_once_with(fake_file_path, "r")
#     expected = len(file_content_mock.split("\n"))
#     assertEqual(expected, actual)


# def test_run_aggregate_query() -> None:

#     pass
