def run():
    #beep is going to a bakery
    #which item from the bakery
    print("What shall I buy from the bakery?")
    purchase = str(input())
    #what size of item
    print("Which size shall I buy?")
    size = str(input())
    if (purchase == "donut") and (size == "big"):
        print("That is too much for me!")
        #ask for a secondary item
        print("What should i get instead?")
        purchase2 = str(input())
        if (purchase2 == "sandwich") or (purchase2 == "roll"):
            print("This will do.")
    elif (purchase == "donut") and (size == "medium"):
        print("This is perfect for me!")
if __name__ == "__main__":
    run()