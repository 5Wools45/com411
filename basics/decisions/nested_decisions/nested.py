def run():
    print("What type of cover does the book have?")
    #ask the user for an input
    cover = str(input())
    if cover == "soft":
        print("Is this book perfect bound?")
        perfect_bound = str(input())
        if perfect_bound == "yes":
            print("Soft cover, perfect bound books are the best")
        else:
            print("Soft covers with coils or stitches are great for short books")
    elif cover == "hard":
        print("Books with hard covers can be more expensive")
    else:
        print("All books are good!")
if __name__ == "__main__":
    run()