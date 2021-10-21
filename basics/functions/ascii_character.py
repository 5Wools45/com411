def run():
    print("Program Started")
    print("Please enter an Ascii code")
    ascii_code = int(input())

    if ascii_code > 31 and ascii_code < 127:
        print(f"The character represented by the ascii code {ascii_code} is {chr(ascii_code)}.")
    else:
        "Please enter a value within the printable ascii character boundaries (32-126)"

    print("Program Ended")
if __name__ == "__main__":
    run()
