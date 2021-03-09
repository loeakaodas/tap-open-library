#!/usr/bin/env python3

import requests
from datetime import datetime as dt


def get_recent_changes(config):
    """Retrieve records from Open Libraries recent-changes API

    Args:
    - config (dict): expects a dict with a `kind` of changes enumerated
        in the tap schema and the `change_date` for which the changes are
        to be retrieved

    Returns:
    - records (list): array of JSON (dict) objects/records from API call

    Notes:
    - See documentation for additional API info at:
        https://openlibrary.org/dev/docs/api/recentchanges
    """
    kind = config["kind"]
    change_date = dt.strptime(config["change_date"], "%Y-%m-%d")

    year = str(change_date.year) + "/"
    month = f"{change_date.month:02d}" + "/"
    day = f"{change_date.day:02d}" + "/"

    url = f"https://openlibrary.org/recentchanges/{year}{month}{day}{kind}.json"
    records = requests.get(url)

    return records.json()
