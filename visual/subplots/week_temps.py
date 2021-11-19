import csv
import matplotlib.pyplot as plt


def read_data():
    data = {}
    with open("temps.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = {'week1': [], 'week2': []}
        for values in csv_reader:
            data['week1'].append(values[0])
            data['week2'].append(values[1])
    return data


def run():
    data = read_data()
    days = range(1, 8)
    fig, axes = plt.subplots(1, 2, sharex='col')
    axes[0].plot(days, data['week1'])
    axes[1].plot(days, data['week2'])
    plt.tight_layout()
    plt.show()


run()
