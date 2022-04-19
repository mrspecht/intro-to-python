# Nested dictionaries

users = {
    "andrespecht": {
        "name": "Andre Specht",
        "email": "andre@email.com"
    },
    "john32": {
        "name": "John Henry",
        "email": "jonh32@email.net"
    }
}

for username, info in users.items():
    print (f"User: {username}")
    print (f"Name: {info['name']}")
    print (f"Email: {info['email']}\n")
