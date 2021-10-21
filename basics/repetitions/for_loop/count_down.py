def run():
    print("How far are we from the cave?")
    steps = int(input())
    for count in range(steps, 0, -1):
        print(f"{count} steps remaining.")
    print("We have reached the cave!")
if __name__ == "__main__":
    run()