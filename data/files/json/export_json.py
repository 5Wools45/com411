import json


def read(path):
    with open(path) as file:
        data = json.load(file)
    print("Reading...\nDone!")
    return data


def save(export_file, json_data):
    print("Exporting...")
    with open(export_file, "w") as file:
        json.dump(json_data, file, indent=4)
    print("Done!")


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()