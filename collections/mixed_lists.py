# Mixed lists

mixture = [1, 2, 3, "one", "two", "three"]
print(type(mixture))

name = input("What is your name? ")
age = input("What is your age? ")
dob = input("What is your DOB? ")
height = input("What is your height? ")
user_details_list = [name, int(age), dob, float(height)]
print(user_details_list)
print("Hi " + user_details_list[0])
print(user_details_list[1])
print(user_details_list[2])
print(user_details_list[3])