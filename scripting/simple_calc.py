# simple calc function
from math_operators import *

user_task = input("What operation? ")
if user_task:
    first_num = int(input("ENTER YOUR FIRST NUMBER: "))
    second_num = int(input("ENTER YOUR SECOND NUMBER: "))
else:
    print("Please select add,subtract,divide or multiply ")
stop_calc = False

if user_task == "add":
    result = add(first_num, second_num)
    print(f"{first_num} + {second_num} = {result}")
elif user_task == "subtract":
    result = subtract(first_num, second_num)
    print(f"{first_num} - {second_num} = {result}")
elif user_task == "divide":
    result = divide(first_num, second_num)
    print(f"{first_num} / {second_num} = {result}")
elif user_task == "multiply":
    result = multiply(first_num, second_num)
    print(f"{first_num} * {second_num} = {result}")
else:
    print("Please select add,subtract,divide or multiply ")

# A package is multiple modules (which are files), so a package would be multiple files
# A library is a general term which is the biggest out of all of them (Usually Large packages)
