import logging
import pytest
from unittest import mock
from datasette.my_example import initialize_db

LOGGER = logging.getLogger(__name__)


def test_initialize_db() -> None:
    # LOGGER.info("Testing initialize DB")
    with mock.patch("datasette.my_example.requests") as mock_requests:
        # SG: I usually prefer to patch objects using a context manager.
        # The behavior should be pretty much equivalent to the decorator.

        # Ex-1
        # mock_response = _mock_response(status=500,
        #  raise_for_status=HTTPError)
        # mock_requests.return_value = mock_response
        # with pytest.raises(requests.exceptions.HTTPError):
        #     initialize_db()
        # Ex-2
        # mock_resp = requests.models.Response()
        # mock_resp.status_code = 404
        # mock_requests.return_value = mock_resp
        # res = requests.get()
        # with pytest.raises(requests.exceptions.HTTPError) as err_msg:
        #     res.raise_for_status()
        # print(err_msg)

        # Ex-3
        mock_requests.get.side_effect = Exception
        with pytest.raises(Exception):
            initialize_db()
            # mock_requests.get.assert_called_once() This row is not needed
            # as it throws exception a the prev line
        return
