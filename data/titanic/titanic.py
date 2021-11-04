import csv

records = []
headings = []


def load_data(file_path):
    print("Loading Data...")
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

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


def display_passenger_names():
    print("The names of the passengers are:")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived")


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == 'male':
            males += 1
        else:
            females += 1

    print(f"Females: {females}, Males: {males}")


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    else:
        print("Error! Option not recognised")


if __name__ == "__main__":
    run()