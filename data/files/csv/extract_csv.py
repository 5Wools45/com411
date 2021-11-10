import csv


def extract(path):
    print("Extracting...")
    names = ""
    with open(path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for lines in csv_reader:
            names += f"{lines[1]}\n"
        print("Done! The extracted names are as follows:")
        print(f"\n{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
