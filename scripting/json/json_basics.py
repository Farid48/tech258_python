import json

car_data = {
    "Name": "tesla",
    "Engine": "Electric"
}

# json.dumps() --> Serialises json to a formatted string which is on the same file

car_data_json_string = json.dumps(car_data)
print(car_data_json_string)

# json.dump() --> creates a stream object and expects a file object to write to (Creates a JSON file object separately and on its own)

with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)
