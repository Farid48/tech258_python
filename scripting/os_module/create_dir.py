import os

# Directory
directory = "test_dir"

# Parent Directory
parent_directory = "c:/Users/Farid/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Create DIR

os.mkdir(path)
