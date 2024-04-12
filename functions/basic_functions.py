# Functions

# DRY - DON'T REPEAT YOURSELF

# Function with no arguments
# def print_something():
#     print("hello world")
# print_something()


# function with arguments

# def print_something(name):
#     print(f"hello nmy name is {name}")
#
#
# print_something("NI HAO")
#
#
# # def addition(num1, num2):
# #     return num1 + num2
# #
# #
# # print(addition(1, 2))
#
# # can still be reformed if you change the value of the arguements
# def addition(int1=2, int2=2):
#     return int1 + int2
#
#
# print(addition(1, 2))

# Multiple arguments

# def multi_args(*multiargs):
#     for i in multiargs:
#         print(i)
#
# multi_args(1,2,3,4,5,6,7)


# type hints

def division(denom: int, num: int) -> float:
    return denom / num


print(division(5, 2))
