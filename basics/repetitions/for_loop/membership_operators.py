print("What phrase do you see?")
phrase = str(input())
print("\nReversing...")
print("\nThe phrase is: ")
reversed = ""

for characters in phrase:
    reversed = characters + reversed
print(reversed)
