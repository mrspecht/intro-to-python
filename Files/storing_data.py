# Storing data with json

import json

file = "data.json"

person = {
    "name": "Andre Specht",
    "role": "Instructor",
    "dept": "IT",
    "courses": [
        "JavaScript",
        "Java",
        "Python"
    ]
}

with open(file, "w") as f:
    json.dump(person, f)

with open(file, "r") as f:
    data = json.load(f)
    print(data)                                                                 # Dictionary


str = json.dumps(person, indent=4)                                              # json.dumps() takes in a json object and returns a string
print(str)

obj = json.loads(str)                                                           # json.loads() takes in a string and returns a json object
print(obj["name"])
