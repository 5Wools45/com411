def run():
    print("What type of book is this?")
    # determining the type of book
    type = str(input())
    #if the book is adventure
    if type == "adventure":
        print("I like adventure books!")
    print("Finished reading book")
if __name__ == "__main__":
    run()