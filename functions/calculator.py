def addition(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def subtraction(num1, num2):
    return num1 - num2


user_task = input("Addition, subtraction, multiplication or division? ")
stop_calc = False


while not stop_calc:

    if user_task == "addition":
        stop_func = False
        while not stop_func:
            num1 = input("What is your first number? ")
            num2 = input("What is your second number? ")
            print(addition(int(num1), int(num2)))
            keep_func = input("Would you like to continue with addition")
            if keep_func == "no":
                stop_func = True
                user_task = input("Please select addition, subtraction, multiplication or division? ")
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




