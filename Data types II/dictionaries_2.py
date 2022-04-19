# Dictionaries (get)

person = {
    "name": "Andre Specht",
    "email": "andrespecht@email.com",
    "role": "IT instructor",
    "courses": [
        "Web desing", "JavaScript", "Java", "Python"
    ]
}

info = input("Enter name, email, role, or courses: ")
data = person.get(info, "Invalid key. Try again")                               # By default, get() returns 'None' when the key doesn't exist
print(data)
