from typing import List, Tuple
import requests

from foldingathome.donor import ShallowDonor


class TeamMember(ShallowDonor):
    def __init__(self, member_row):
        super().__init__(member_row[0], member_row[1], member_row[3], member_row[4])
        self.rank = member_row[2]


class Team(ShallowDonor):
    def __init__(self, team: int):
        r = requests.get(f"https://api2.foldingathome.org/team/{team}")

        if r.status_code != 200:
            raise requests.RequestException(r.content)

        raw_data = r.json()

        super().__init__(
            raw_data["name"], raw_data["id"], raw_data["score"], raw_data["wus"]
        )
        self.founder: str = raw_data["founder"]
        self.url: str = raw_data["url"]
        self.logo: str = raw_data["logo"]
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
