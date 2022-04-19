# Handling exceptions

txt = "my-passwords.txt"

try:
    with open(txt, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Passwords must be... secret")
