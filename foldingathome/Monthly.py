import requests


class Monthly:
    def __init__(self):
        target = "https://stats.foldingathome.org/api"
        r = requests.get(f"{target}/teams-monthly")
        self.teams = r.json()
        self.Teams = self.Teams(self.teams)

    class Teams:
        def __init__(self, input):
            self.teams = input

        def highest_scorer(self):
            teams = self.teams["results"]
            teams_and_scores = {}
            scores = []
            for team in teams:
                teams_and_scores[team["name"]] = team["credit"]
                scores.append(team["credit"])

            credit = max(scores)
            wus = teams[scores.index(credit)]["wus"]
            rank = teams[scores.index(credit)]["rank"]
            team = teams[scores.index(credit)]["team"]
            name = teams[scores.index(credit)]["name"]

            return {
                "wus": wus,
                "name": name,
                "rank": rank,
                "credit": credit,
                "team": team
            }

        def most_wus(self):
            teams = self.teams["results"]
            teams_and_scores = {}
            wus = []
            for team in teams:
                teams_and_scores[team["name"]] = team["wus"]
                wus.append(team["wus"])
            work_units = max(wus)

            credit = teams[wus.index(work_units)]["credit"]
            rank = teams[wus.index(work_units)]["rank"]
            team = teams[wus.index(work_units)]["team"]
            name = teams[wus.index(work_units)]["name"]

            return {
                "wus": work_units,
                "name": name,
                "rank": rank,
                "credit": credit,
                "team": team
            }

        def team_list(self):
            return self.teams["results"]
