from typing import List, Tuple
import requests


class TeamMember:
    def __init__(self, member_row):
        self.name = member_row[0]
        self.id = member_row[1]
        self.rank = member_row[2]
        self.score = member_row[3]
        self.wus = member_row[4]


class Team:
    def __init__(self, team: int):
        r = requests.get(f"https://api2.foldingathome.org/team/{team}")

        if r.status_code != 200:
            raise requests.RequestException(r.content)

        raw_data = r.json()
        self.id: int = raw_data["id"]
        self.name: str = raw_data["name"]
        self.founder: str = raw_data["founder"]
        self.url: str = raw_data["url"]
        self.logo: str = raw_data["logo"]
        self.score: int = raw_data["score"]
        self.wus: int = raw_data["wus"]
        self.rank: int = raw_data["rank"]

    def members_raw(self) -> List[Tuple[str, int, int, int, int]]:
        r = requests.get(f"https://api2.foldingathome.org/team/{self.id}/members")

        r.raise_for_status()

        return r.json()

    def members(self) -> List[TeamMember]:
        """
        Returns the top 1000 members of the team.

        This function does extra computation to leave the data in a format
        that is slightly easier to use. Use `members_raw()` if you don't want
        that.
        """
        raw = self.members_raw()

        return [TeamMember(member_row) for member_row in raw[1:]]
