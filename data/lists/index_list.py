def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    path = movements()
    for index in range(0, len(path), 2):
        print(f"{path[index]} for {path[index+1]} steps")

if __name__ == "__main__":
    run()
