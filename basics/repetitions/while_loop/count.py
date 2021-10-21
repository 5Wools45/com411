def run():
    print("How many live cables must i avoid?")
    #ask the user to input how many cables
    cables_to_avoid = int(input())
    #creating a variable to track the number of live cables
    cables_avoided = 0
    while cables_avoided < cables_to_avoid:
        print("Avoiding...", end="")
        cables_avoided +=1
        print(f"Done! {cables_avoided} cables avoided")
if __name__ == "__main__":
    run()