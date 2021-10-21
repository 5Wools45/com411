def run():
    print("Calculating the sum of the first 100 numbers")
    number = 1
    total = 0
    while number <= 100:
        total = total + number
        number +=1
        print(f"...Done! The answer is {total}")
if __name__ == "__main__":
    run()