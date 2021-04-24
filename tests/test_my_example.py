import logging
from datetime import datetime
from datasette.my_example import initialize_db

LOGGER = logging.getLogger(__name__)


def test_initialize_db():
    now = datetime.now()
    LOGGER.info("Testing now.")
    timestamp = initialize_db(now)
    assert timestamp == now
