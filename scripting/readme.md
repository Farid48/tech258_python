# Scripting

## What is Scripting? How does it differ from coding?
* Coding/Programming is a general term and an umbrella for all computer languages
* Scripting is code used to automate processes
* Can be used to make content dynamic, such as using JavaScript when creating websites
* Scripting languages would not be used to create static features (website layouts)

# Python Standard Library -What are the Packages?
1) OS - Used to provided functions to interact with the Operating System (OS)
```python
import os

# Can the directory of where the file is located
working_dir = os.getcwd()
print(f"current working directory is: {working_dir}")

# Can count the CPU Cores

cpu_cores = os.cpu_count()
print(f"amount of cores: {cpu_cores}")
```
2) datetime - Very useful to obtain data about the current date/time, which can be used for various applications
```python
import datetime

print(f"today date is:{datetime.datetime.today()}")
```
3) math - Very useful for more advanced mathematics formulas 
```python
import math
num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
print(f"remainder from 1/5: {math.remainder(1,5)}")
```

# Python Scripts a DevOps Engineer may create:
1) Automated Deployment Script: Automates the deployment of applications or infrastructure
2) Monitoring Script: Collects and analyses system metrics for servers or applications
3) Backup Script: Automates the backup
4) Configuration Management Script: Manages configuration files across multiple servers or environments
5) Alerting Script: Monitors system health.