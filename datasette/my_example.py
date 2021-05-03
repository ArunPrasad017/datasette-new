"""
"""
import logging
from datetime import datetime

import requests
import sqlite_utils

log = logging.getLogger(__name__)


def initialize_db(timestamp):
    print(f"Inside the docker file at - {timestamp}")
    log.debug("This is a debugging message")
    db = sqlite_utils.Database("meteorites.db")
    db["meteorites"].insert_all(
        requests.get("https://data.nasa.gov/resource/y77d-th95.json").json(),
        pk="id",
    )
    return timestamp


def main():
    now = datetime.now()
    initialize_db(now)


if __name__ == "__main__":
    main()
