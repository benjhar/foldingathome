import requests


class Team:
    def __init__(self, team=0):
        r = requests.get(f"https://stats.foldingathome.org/api/team/{team}")
        self.team = r.json()
        self.donors = r.json()["donors"]
        self.total_teams = self.team["total_teams"]
        self.name = self.team["name"]
        self.score = self.team["credit"]
        self.work_units = self.team["wus"]
        self.total_donors = len(self.team["donors"])
        self.total_teams = self.team["total_teams"]
        self.rank = self.team["rank"]
        self.logo = self.team["logo"]
        self.stats = self.team

    def highest_scorer(self):
        donors = self.donors
        users_and_scores = {}
        scores = []
        wus = []
        for donor in donors:
            users_and_scores[donor["name"]] = donor["credit"]
            scores.append(donor["credit"])
        credit = max(scores)
        wus = donors[scores.index(credit)]["wus"]
        rank = donors[scores.index(credit)]["rank"]
        team = donors[scores.index(credit)]["team"]
        id = donors[scores.index(credit)]["id"]
        name = donors[scores.index(credit)]["name"]

        return {
            "wus": wus,
            "name": name,
            "rank": rank,
            "credit": credit,
            "team": team,
            "id": id,
        }

    def most_wus(self):
        donors = self.donors
        users_and_scores = {}
        wus = []
        for donor in donors:
            users_and_scores[donor["name"]] = donor["wus"]
            wus.append(donor["wus"])
        work_units = max(wus)

        credit = donors[wus.index(work_units)]["credit"]
        rank = donors[wus.index(work_units)]["rank"]
        team = donors[wus.index(work_units)]["team"]
        id = donors[wus.index(work_units)]["id"]
        name = donors[wus.index(work_units)]["name"]

        return {
            "wus": work_units,
            "name": name,
            "rank": rank,
            "credit": credit,
            "team": team,
            "id": id,
        }
