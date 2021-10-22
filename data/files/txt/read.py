def display_chars(path, chars):
    with open(path) as file:
        data = file.read(chars)
        print(data)

def display_line(path):
    with open(path) as file:
        line = file.readline().strip()
        print(line)

def display_text(path):
    with open(path) as file:
        text = file.read()
        print(text)



def run():
    path = "library.txt"
    display_chars(path, 5)
    display_line(path)
    display_text(path)

if __name__ == "__main__":
    run()