#ask the user for 3 whole numbers
print("Please enter the first whole number")
number1 = int(input())
print("Please enter the second whole number")
number2 = int(input())
print("Please enter the third whole number")
number3 = int(input())
# i = number of even numbers, x = number of odd numbers
i = 0
x = 0
#increase each variable by 1 each time they are found to be divisible by 2 or not
if number1 % 2 == 0:
    i += 1
else:
    x += 1
if number2 % 2 ==0:
    i += 1
else:
    x += 1
if number3 % 2 ==0:
    i += 1
else:
    x += 1


print(f"There are {i} even numbers")
print(f"There are {x} odd numbers")





