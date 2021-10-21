def run():
    print("How many numbers should I sum up?")
    number_count = int(input())
    running_total = 0
    numbers_inputted = 1
    while numbers_inputted <= number_count:
        print(f"Please enter number {numbers_inputted} of {number_count}")
        numbers_inputted +=1
        running_total = int(input()) + running_total
    print(f"The answer is {running_total}")

if __name__ == "__main__":
    run()