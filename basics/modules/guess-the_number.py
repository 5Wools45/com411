import random as rnd
print("Please enter the minimum value.")
minvalue = int(input())
print("Please enter the maximum value.")
maxvalue = int(input())
rand_value = rnd.randrange(minvalue, maxvalue, 1)
print(f"I am thinking of a number between {minvalue} and {maxvalue}. Can you guess what it is?")

guessed_correctly = False

while not guessed_correctly:
    print("Please enter a number:")
    guess = int(input())

    if guess == rand_value:
        print("Congratulaions, you have guessed the correct number!")
        guessed_correctly = True
    elif guess < rand_value:
        print("Guess higher.")
    else:
        print("Guess lower.")
print("Game Over")
