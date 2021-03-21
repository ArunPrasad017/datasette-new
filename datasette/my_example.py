"""
"""
import requests
import sqlite_utils

print("Inside the docker file")
db = sqlite_utils.Database("meteorites.db")
db["meteorites"].insert_all(
    requests.get("https://data.nasa.gov/resource/y77d-th95.json").json(), pk="id"
)