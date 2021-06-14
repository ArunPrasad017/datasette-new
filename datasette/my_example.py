"""
"""
from os import path
import logging

import requests
import sqlite_utils

log = logging.getLogger(__name__)

url = "https://datahub.io/sports-data/spanish-la-liga/r/season-1819.json"


def initialize_db() -> None:
    db = sqlite_utils.Database("laliga1819.db")
    try:
        r = requests.get(url)
        r.raise_for_status()
        if r.status_code == 200:
            db["laliga1819"].insert_all(
                requests.get(url).json(),
                pk="id",
            )
    except Exception as e:
        log.debug(f"Failed due to: {e}")
        raise Exception


def _read_sql(filename: str) -> str:
    log.info("Read SQL file")
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "..", filename))
    with open(filepath, "r") as fd:
        sqlFile = fd.read()
    return sqlFile


def run_aggregate_query() -> None:
    file_name = "agg_query"
    sqlFile = _read_sql(file_name)
    try:
        db = sqlite_utils.Database("laliga1819.db")
    except Exception as E:
        log.error("DB not found - Exception: {}".format(E))
        raise Exception
    log.info("Executing SQL file on laliga db")
    db.execute(sqlFile)


def main() -> None:
    initialize_db()
    run_aggregate_query()


if __name__ == "__main__":
    main()
