import os

# Directory
directory = "test_dir"

# Parent Directory
parent_directory = "c:/Users/Farid/Documents"

# Path
path = os.path.join(parent_directory, directory)

# filename
filename = "testfile.txt"

# filepath
filepath = os.path.join(path,filename)

# Create the file
with open(filepath, "w") as file1:
    toFile = "Contents of the file go here"
    file1.write(toFile)
