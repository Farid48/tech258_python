# task 3 While loops:

# x = 0
#
# while x <10:
#     print(f"x -> {x}")
#     x += 1
#
# If there was no increment, no the while loop wouldn't stop and can cause crashes

# Task 4:
# 1)
user_prompt = True
while user_prompt == True:
    age = input("What is your age? ")
    if age.isdigit() and int(age) <= 117:
        user_prompt = False
    else:
        print("Please enter your real age")
print(f"Your age is {age}")


