import tui
medal_column = 14
team_column = 6
year_column = 9

def list_years(data):
    #data is a list
    tui.started(f"Extracting distinct years from {data}")
    year_set = set()
    for record in data:
        year = record[year_column]
        year_set.add(year)
    tui.display_years(year_set)
    tui.completed()
