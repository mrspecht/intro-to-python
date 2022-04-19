# for loops (tuples and dictionaries)

friends = (                                                                     # A tuple with 3 tuples
    ('John', "johnyork@email.com"),
    ('Terry', "imterry@supermail.com"),
    ('Mary', "mary27@emai.net")
)

for name, email in friends:                                                     # Unpacking
    print(f"{name}'s email is {email}")


person = {
    "name": "Andre Specht",
    "role": "IT instructor",
    "email": "andrespecht@email.com",
    "course": "Python"
}

for key in person:
    print(f"{key.title()} \t {person[key]}")


info = person.items()                                                           # dict_items([]) returns a list with key-value pairs
print(info)

for key, value in info:
    print(f"Key: {key.title()} \t Value: {value}")
