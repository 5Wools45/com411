def run():
    print("Program Started")
    print("Please enter a standard character")
    character = input()

    if len(character) == 1:
        print(f"The ascii code for {character} is {ord(character)}")
    else:
        print("Please only enter one character")
    print("Program ended")
if __name__ == "__main__":
    run()