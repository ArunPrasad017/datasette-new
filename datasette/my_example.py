"""
"""
import logging
from datetime import datetime

import requests
import sqlite_utils

log = logging.getLogger(__name__)

url = "https://datahub.io/sports-data/spanish-la-liga/r/season-1819.json"


def initialize_db(timestamp: datetime) -> datetime:
    db = sqlite_utils.Database("laliga1819.db")
    db["laliga1819"].insert_all(
        requests.get(url).json(),
        pk="id",
    )
    return timestamp


def run_aggregate_query() -> None:
    with open("agg_query.sql", "r") as fd:
        sqlFile = fd.read()
    db = sqlite_utils.Database(sqlite_utils.connect("my_database.db"))
    db.execute(sqlFile)


def main() -> None:
    now = datetime.now()
    initialize_db(now)
    run_aggregate_query()


if __name__ == "__main__":
    main()
