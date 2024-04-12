def addition(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def subtraction(num1, num2):
    return num1 - num2


user_task = input("Addition, subtraction, multiplication or division? ")

if user_task == "addition":
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")
    print(addition(int(num1), int(num2)))
elif user_task == "subtraction":
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")
    print(subtraction(int(num1), int(num2)))
elif user_task == "multiplication":
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")
    print(multiply(int(num1), int(num2)))
elif user_task == "division":
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")
    print(division(int(num1), int(num2)))
else:
    print("Please select Addition, subtraction, multiplication or division? ")

