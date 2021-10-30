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


def display_menu():
    print("\"\"\"")
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that arrived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")
    print("\"\"\"")
    response = int(input())
    return response


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")




run()

