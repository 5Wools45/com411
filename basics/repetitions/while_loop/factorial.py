def run():
    print("Please enter a number?")
    number = int(input())
    #count must start multiplying by 1
    total = 1
    #count increases once every iteration for the factorial
    count = 0
    while count < number:
        count +=1
        total = total * count
    print(f"The factorial is {total}.")

if __name__ == "__main__":
    run()