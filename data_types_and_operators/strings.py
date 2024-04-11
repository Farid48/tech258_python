# Strings

#String Slicing

hw = "Hello World!"

# find out how many characters are in this String
print(len(hw))
# Target just the first character (H)
print(hw[0])
# Target the last character
print(hw[-1])
# use negative indexing to get the second to last character
print(hw[-2])
# Use string slicing to get the first 3 characters only
print(hw[0:3])


# String methods

white_space = "Lot's of white space at the end              "
print(len(white_space.strip()))

# count a substriing within a string

example_string = "Here's some text with lot's of text"
print(example_string.count("text"))
print(example_string.upper())
print(example_string.lower())
print(example_string.capitalize()) # only does the first word
print(example_string.replace("with", "NO"))

# concatenation

a = "here "
b = "more "
c = "much more"

print(a + b + c)

x = 2
y = 5.4
z = " there's now a numebr 25.4 unless we put a space in!"

print(str(x) + " " + str(y) + " " + z)

# f-strings

name = "lassie"
years = 8
height_cm = 79.1

print(f"{name} is {years} old and {height_cm} tall")

name = "snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")

#using f strings to format numbers

pi = 3.14159265359

# use an f string to print pi to 3 decimal places
print(f"{round(pi,3)}")
print(f"{pi:.3f}")
# use f string to print pi to 5 decimal places
print(f"{round(pi,5)}")
print(f"{pi:.5f}")

score = 16
max_score = 26

print(f"YOu scored {score/max_score}")
print(f"You scored {score/max_score:.2%}")






