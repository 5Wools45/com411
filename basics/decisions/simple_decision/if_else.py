def run():
    print("Please enter the activity to be performed")
    #ask for an input for activity
    i = str(input())
    if i == "calculate":
        print("Performing Calculations...")
    else:
        print("Performing Activity")
    print("Activity Completed!")
if __name__ == "__main__":
    run()