"""
"""
import logging

import requests
import sqlite_utils

log = logging.getLogger(__name__)

url = "https://datahub.io/sports-data/spanish-la-liga/r/season-1819.json"


def initialize_db() -> None:
    db = sqlite_utils.Database("laliga1819.db")
    try:
        db["laliga1819"].insert_all(
            requests.get(url).json(),
            pk="id",
        )
    except requests.ConnectionError:
        log.error("URL undefined")
        return None
    return


def run_aggregate_query() -> None:
    log.info("Read SQL file")
    with open("agg_query.sql", "r") as fd:
        sqlFile = fd.read()
    try:
        db = sqlite_utils.Database("laliga1819.db")
    except Exception as E:
        log.error("DB not found - Exception: {}".format(E))
        return
    log.info("Executing SQL file on laliga db")
    db.execute(sqlFile)


def main() -> None:
    initialize_db()
    run_aggregate_query()


if __name__ == "__main__":
    main()
