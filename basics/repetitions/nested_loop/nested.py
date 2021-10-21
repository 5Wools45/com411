def run():
    print("How many rows should I have?")
    rows = int(input())

    print("How many columns should I have?")

    cols = int(input())

    print("\nHere I go:")

    for row in range(rows):
        for col in range(cols):
            print(":-)", end="")
        print()
if __name__ == "__main__":
    run()