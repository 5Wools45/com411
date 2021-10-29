def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(0, len(direction), 1):
        print(f"{index}: {direction[index]}")


def run():
    if __name__ == "__main__":
        menu()


run()
