import json

# .load examples
# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile) # Converts it into a dictionary
#     print(type(car))
#     print(car["Name"])
#     print(car["Engine"])


path_to_json = "example.json"
json = json.loads(open(path_to_json).read())
value = json["name"]
print(value)

#json.load takes a file
#json.loads takes a string