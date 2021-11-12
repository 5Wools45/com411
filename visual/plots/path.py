import matplotlib.pyplot as plt


def coordinate():
    print("Please enter an 'X' value:")
    x = input()
    print("Please enter a 'Y' value:")
    y = input()
    return x, y


def path():
    print("Retrieving Path...")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return x_values, y_values


def run():
    values = path()
    x = values[0]
    y = values[1]
    print(f"{x},{y}")
    plt.plot(x, y, "ro--")
    plt.show()


run()
