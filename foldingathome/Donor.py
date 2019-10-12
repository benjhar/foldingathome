import requests


class Donor:
    def __init__(self, donorname, team=0):
        r = requests.get(f"https://stats.foldingathome.org/api/team/{team}")
        self.team = r.json()

        donors = self.team["donors"]
        found = False
        for donor in donors:
            if donor["name"] == str(donorname):
                self.donor = donor
                found = True
        if not found and team == 0:
            raise Exception(
                f"\n\nNo user could be fou  nd with that name: {donorname}.\n This could be due to the user not being on the leaderboard for the default team, as the api only displays the top 1000 members of a team."
            )
            return
        elif not found:
            raise Exception(f"\n\nNo user could be found with that name: {donorname}")
            return

        self.name = self.donor["name"]
        self.id = self.donor["id"]
        self.score = self.donor["score"]
        self.work_units = self.donor["work_units"]
        self.team_id = self.team["team"]

    def rank(self):
        donors = self.team["donors"]
        scores = []
        order = []
        for donor in donors:
            scores.append(donor["credit"])
        for i in scores:
            order.append(max(scores))
            scores.pop(scores.index(max(scores)))
            return order.index(self.donor["credit"]) + 1
