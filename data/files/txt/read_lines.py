def search(file):
    print("Searching...")
    with open(file) as data:
        for line in data:
            print(f"Looked in {line.strip()}")
        print("...Done!")

def run():
    file = "library.txt"
    search(file)

if __name__ == "__main__":
    run()