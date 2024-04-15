import json
import os.path
import sys

# print(f"This is the name of the program: {sys.argv[0]}")
# print(f"Number of elements including the name of the program: {len(sys.argv)}")
# print(f"Number of elements excluding the name of the program: {(len(sys.argv)-1)}")
# print(f"Argument List: {str(sys.argv)}")

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]): # Check if taht second argument is actually a file name and if it exists
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON IS VALID!")
    else:
        print(sys.argv[1] + "NOT FOUND")
else:
    print("Usage: Python check_json.py <file>")

