# Working with files

file = input("Enter a file name: " )
file = f"{file}.txt"

message = input("Enter a message: ")

with open(file, "w") as f:
    f.write(message)
    f.close()

print(f"My file: {file}")
print(f"My message: {message}")
print("Message saved successfully")
