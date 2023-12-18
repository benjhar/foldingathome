from foldingathome.donor import ShallowDonor
from typing import List
import requests


def top_monthly_donors_raw(month: int, year: int) -> List[dict]:
    r = requests.get(
        f"https://api2.foldingathome.org/user/monthly?month={month}&year={year}"
    )

    r.raise_for_status()

    return r.json()


def top_monthly_donors(month: int, year: int) -> List[ShallowDonor]:
    donors = top_monthly_donors_raw(month, year)

    return [
        ShallowDonor(don["name"], don["id"], don["credit"], don["wus"])
        for don in donors
    ]


def top_monthly_teams_raw(month: int, year: int) -> List[dict]:
    r = requests.get(
        f"https://api2.foldingathome.org/team/monthly?month={month}&year={year}"
    )

    r.raise_for_status()

    return r.json()


def top_monthly_teams(month: int, year: int) -> List[ShallowDonor]:
    teams = top_monthly_teams_raw(month, year)

    return [
        ShallowDonor(team["name"], team["team"], team["credit"], team["wus"])
        for team in teams
    ]
