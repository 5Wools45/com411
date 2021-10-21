def run():
    print("How many cables should I remove?")
    number = int(input())
    x = 0
    while x < number:
        print("Removed Cable.")
        x +=1
if __name__ == "__main__":
    run()