def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)


def display_lower(word):
    print(word.lower())

def display_upper(word):
    print(word.upper())

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")


def repeat(word):
    print("How many times should the word be repeated?")
    repetitions = int(input())

    for repetition in range(repetitions):
        if (repetition % 2 == 0):
            print(display_lower(word))
        else:
            print(display_upper(word))



def run():
    print("Please enter a word:")

    word = input()

    print("What would you like to do with this word?")
    print("[1] Display the word in a box")
    print("[2] Display the word in lower case")
    print("[3] Display the word in upper case")
    print("[4] Display the word mirrored")
    print("[5] Display the word repeated")
    print("[6] Quit")

    method = int(input())

    if(method == 1):
        display_box(word)
    elif(method == 2):
        display_lower(word)
    elif(method == 3):
        display_upper(word)
    elif(method) == 4:
        display_mirrored(word)
    elif(method == 5):
        repeat(word)
    else:
        print("Unknown Option")
if __name__ == "__main__":
    run()


