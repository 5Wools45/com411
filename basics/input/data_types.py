#BMI Calculator

print("What is your name Human?")
name = str(input())
print("How old are you (in years)")
age = int(input())
print("How tall are you (in meters)")
height = float(input())
print("How much do you weigh (in KG)")
weight = float(input())
#Calculate BMI
bmi = weight // (height ** 2)
print(f"{name}, you are {age} years old and your BMI is {bmi}")
