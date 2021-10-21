def run():
    #ask user what type of adventure they want
    print("Enter the type of adventure you'd like.")
    adventure = str(input())
    if (adventure == "scary") or (adventure == "short"):
        print("Entering the dark forest")
    elif (adventure == "safe") or (adventure == "long"):
        print("Taking the safe route")
    else:
        print("Not sure which route to take")
if __name__ == "__main__":
    run()