import requests

def total_teams():
    r = requests.get(f'https://stats.foldingathome.org/api/team/0')
    team = r.json()
    return team["total_teams"]

class Team:
    def __init__(self, team=0):
        r = requests.get(f'https://stats.foldingathome.org/api/team/{team}')
        self.team = r.json()
        self.donors = r.json()["donors"]

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
            "id": id
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
            "id": id
        }

    def score(self):
        return self.team["credit"]

    def work_units(self):
        return self.team["wus"]

    def total_donors(self):
        return len(self.team["donors"])

    def rank(self):
        return self.team["rank"]

    def logo(self):
        return self.team["logo"]

    def stats(self):
        return self.team
