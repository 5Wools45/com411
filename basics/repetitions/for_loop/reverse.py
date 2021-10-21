def run():
    print("What phrase do you see?")
    phrase = str(input())
    print("\nReversing...")
    print("\nThe phrase is ", end = "")
    for position in range(len(phrase) -1, -1, -1):
        print(phrase[position], end = "")
if __name__ == "__main__":
    run()