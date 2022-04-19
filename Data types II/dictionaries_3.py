# Looping through a dictionary

person = {
    "name": "Andre Specht",
    "email": "andrespecht@email.com",
    "role": "IT instructor",
    "courses": [
        "Web desing", "JavaScript", "Java", "Python"
    ]
}

for key, value in person.items():                                               # items() returns a list with key-value pairs
    print (key, "->", value)                                                    # Printing with parameters (3 objects)
