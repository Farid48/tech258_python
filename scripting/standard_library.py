# Python standard library

# Standard library consists of modules and packages that are useful, so they are added by default

import random
import math
import os
import sys
import datetime
import builtins
import requests

# print(random.random())
# print(random.randrange(1,10))

# math demos

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
print(f"remainder from 1/5: {math.remainder(1,5)}")

#OS
working_dir = os.getcwd()
print(f"current working directory is: {working_dir}")

# get current user

username = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"username is {username}")

# cpu cores

cpu_cores = os.cpu_count()
print(f"amount of cores: {cpu_cores}")

# # make directory
# os.mkdir("test_dir")

# sys demo

print(f"current path {sys.path}")
print(sys.version)


# date time

print(f"today date is:{datetime.datetime.today()}")


# builtins demo

# for name in dir(builtins):
#     if name[0].islower():
#         print(name)

# request demo

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)