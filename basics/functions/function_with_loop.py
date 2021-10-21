def cross_bridge(steps):
    for step in range(steps):
        print("Crossed Step")

    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")
if __name__ == "__main__":

    cross_bridge(3)
    cross_bridge(6)
