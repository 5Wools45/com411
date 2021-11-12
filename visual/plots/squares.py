import matplotlib.pyplot as plt


def small():
    x_values = [3, 3, 4, 4, 3]
    y_values = [3, 4, 4, 3, 3]
    plt.plot(x_values, y_values, "ro:")


def medium():
    x_values = [2, 2, 5, 5, 2]
    y_values = [2, 5, 5, 2, 2]
    plt.plot(x_values, y_values, "gs--")


def large():
    x_values = [1, 1, 6, 6, 1]
    y_values = [1, 6, 6, 1, 1]
    plt.plot(x_values, y_values, "bp-")


def run():
    small()
    medium()
    large()
    plt.show()


run()
