import requests

from foldingathome.Team import Team


class TeamRankException(RuntimeError):
    """There was an error getting the user's rank"""


def get_team_from_team_list(name, id, team_list, team_id):
    for team in team_list:
        if team["team"] == team_id:
            return team
    raise TeamRankException(f"{name} ({id}) has not contributed to team ID {team_id}.")


class Donor:
    def __init__(self, donor_id: int = 0):
        self.id = donor_id
        r = requests.get(f"https://api2.foldingathome.org/uid/{self.id}")

        r.raise_for_status()

        raw_data = r.json()

        self.name: str = raw_data["name"]
        self.score: int = raw_data["score"]
        self.work_units: int = raw_data["wus"]
        self.rank: int = raw_data["rank"]
        self.active_50: int = raw_data["active_50"]
        self.active_7: int = raw_data["active_7"]
        self.teams: dict = raw_data["teams"]

    def team_score(self, team_id: int) -> int:
        team = get_team_from_team_list(self.name, self.id, self.teams, team_id)
        return team["score"]

    def team_wus(self, team_id: int) -> int:
        team = get_team_from_team_list(self.name, self.id, self.teams, team_id)
        return team["wus"]
