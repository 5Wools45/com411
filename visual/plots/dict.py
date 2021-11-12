import matplotlib.pyplot as plt
import random


def data():
    paths = {}
    print("What type of line would you like? (:, -, --)")
    line_input = input()
    print("What colour would you like to use? (r, g, b)")
    colour_input = input()
    print("Which style of marker would you like? (o, s, ^)")
    marker_input = input()
    paths["line"] = line_input
    paths["colour"] = colour_input
    paths["marker"] = marker_input
    return paths


def generate():
    print("How many lines would you like to display?")
    lines = int(input())
    for number in range(lines):
        values = data()
        format = f"{values['colour']}{values['marker']}{values['line']}"
        plt.plot(random.sample(range(1, 100), 50), random.sample(range(1, 100), 50), format)



def run():
    print("Running...")
    generate()
    plt.show()
    print("Done!")


run()
