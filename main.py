print("Hello, Welcome to the game of Tic Tac Toe!")
name = input("Hello once again, please enter your name:")
print("Hello", name, "let's play Tic Tac Toe!")
age = int(input("How old are you?:"))
print("You are", age, "years old.")
height = float(input("How tall are you in meters?:"))
weight = float(input("How much do you weigh in kilograms?:"))
bmi = weight / height ** 2
print("Your BMI is", bmi)
if bmi < 25:
    print("You are in good shape.")
    if bmi < 20:
        print("You are underweight.")
else:
    print("You are overweight.")
