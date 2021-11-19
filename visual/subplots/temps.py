import matplotlib.pyplot as plt


def read_data(file):
    temps = []
    with open(file) as data:
        for line in data:
            temps.append(line.strip())
    return temps


def run():
    data = read_data("temps.txt")
    days = range(1, 8)
    fig, axes = plt.subplots(1, 2, sharex='row')
    axes[0].plot(days, data)
    axes[1].bar(days, data)
    plt.tight_layout()
    plt.show()


run()
