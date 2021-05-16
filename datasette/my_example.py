"""
"""
import logging
from datetime import datetime

import requests
import sqlite_utils

log = logging.getLogger(__name__)

url = "https://datahub.io/sports-data/spanish-la-liga/r/season-1819.json"


def initialize_db(timestamp):
    print(f"Inside the docker file at - {timestamp}")
    log.debug("This is a debugging message")
    db = sqlite_utils.Database("epl1819.db")
    db["epl1819"].insert_all(
        requests.get(url).json(),
        pk="id",
    )
    return timestamp


def main():
    now = datetime.now()
    initialize_db(now)


if __name__ == "__main__":
    main()
