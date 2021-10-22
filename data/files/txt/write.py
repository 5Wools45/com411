def search(path):
    print("Searching...")

    sections = str("")

    books = str("Books:\n")

    with open(path) as data:
         for line in data:
             if "Section" in line:
                 sections += line
             else:
                 books += line
    print("Done!")
    return f"{sections}\n\n{books}"

def save(path,data):
    print("Saving...")
    with open(path, "w") as file:
        file.write(data)
    print("Done!")


def run():
    data = search("books.txt")
    save("exported_books.txt",data)

if __name__ == "__main__":
    run()