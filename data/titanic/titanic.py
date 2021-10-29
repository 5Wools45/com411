import csv

records = []
headings = []

def load_data(file_path):
    print("Loading Data...")
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        global headings
        headings += next(csv_reader)
        for lines in csv_reader:
            global records
            records += (lines)
    print("Done!")


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")

run()

