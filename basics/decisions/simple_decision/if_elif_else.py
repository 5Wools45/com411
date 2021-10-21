def run():
    print("Towards which direction should i paint? (up, down, left or right)")
    #ask for specific input
    i = str(input())
    if i == "up":
        print("I am painting in the upward direction")
    elif i == "down":
        print("I am painting in the downward direction")
    elif i == "left":
        print("I am painting in the left direction")
    elif i == "right":
        print("I am painting in the right direction")
    else:
        print("I dont know which direction i am painting")
    print("I have finished painting")
if __name__ == "__main__":
    run()