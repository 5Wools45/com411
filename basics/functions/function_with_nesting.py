def identify():
    print("What lies before you?")
    response = input()
    if "boulder" in response:
        print("Its time to run!")
    else:
        print("We will be fine.")

identify()
