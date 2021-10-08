#ask user for first number
print("Please enter the first number")
# the first number = i
i = int(input())
#ask user for second number
print("Please enter the second number")
# the second number = x
x = int(input())
if i < x:
    print("The first number is the smallest")
elif i > x:
    print("The second number is the smallest")
else:
    print("Both are equal")