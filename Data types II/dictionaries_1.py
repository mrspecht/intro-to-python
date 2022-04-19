# Dictionaries

person = {                                                                      # Dictionaries are Python’s implementation of a data structure
    "name": "Andre Specht",                                                     # that is more generally known as an associative array. A
    "role": "IT instructor",                                                    # dictionary consists of a collection of key-value pairs. Each
    "age": 37,                                                                  # key-value pair maps the key to its associated value
    "courses": [
        "Web desing", "JavaScript", "Java", "Python"
    ]
}

person["age"] = 38
print(person)

python = person["courses"][3]
print(python)

person["email"] = "andrespecht@email.com"                                       # Inserts new data into the dictionary
person.pop("age")                                                               # Removes 'age' from 'person'; returns the deleted value
print(person)                                                                   # 'del person["age"]' also removes 'age' from 'person'

print(person.keys())                                                            # dict_keys(['name', 'role'...]) | Type <class 'dict_keys'>
print(person.values())                                                          # dict_values([...]) | Type <class 'dict_values'>

person.clear()                                                                  # {}

del person                                                                      # The 'del' keyword is used to delete objects
# print(person)                                                                 # Error: 'person' is not defined
