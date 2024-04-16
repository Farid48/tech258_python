# Python APIs

import requests

postcode_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(postcode_req.headers)
# print(postcode_req.status_code)
# print(postcode_req.content)
# print(type(postcode_req.json()))

data_dict = postcode_req.json()["result"]
print(data_dict["region"])
print(data_dict)

