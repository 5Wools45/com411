def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
    response = int(input())
    return dirs[response]


def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape Route: {route}")


run()


