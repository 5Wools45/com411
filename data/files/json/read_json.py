import json


def read(path):
    with open(path) as file:
        data = json.load(file)
        city = data["city"]
        population = data["population"]
        print(f"City Name: {city} \nPopulation: {population}")
        for bots in data["bots"]:
            name = bots["name"]
            stats = bots["stats"]
            print(f"{name} has the follow {stats}:")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()
