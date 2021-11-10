import tui

medal_column = 14
team_column = 6
year_column = 9


def list_years(data):
    tui.started(f"Extracting distinct years from {data}")
    year_set = set()
    for record in data:
        year = record[year_column]
        year_set.add(year)
    tui.display_years(year_set)
    tui.completed()


def tally_medals(data):
    tui.started("Tallying medals")
    medal_tally = {"Gold": "0", "Silver": "0", "Bronze": "0"}
    for record in data:
        medal = record[medal_column]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    tui.display_medal_tally(medal_tally)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[team_column]
        medal = record[medal_column]
        if medal not in ("Gold", "Silver", "Bronze"):
            continue
        if team in medal_tally:
            medal_tally[team][medal] += 1
        else:
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1
    tui.display_team_medal_tally(medal_tally)
    tui.completed()