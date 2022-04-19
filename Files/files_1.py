# Working with files

with open("heroes.txt", "w") as file:                                           # Write (create)
    file.write("Superman")
    file.write("\nBatman")
    file.write("\nFlash")
    file.write("\nAquaman")
    file.write("\nWonder-Woman")
    file.close()


with open("heroes.txt", "a") as file:                                           # Append
    file.write("\nCyborg")
    file.close()


with open("heroes.txt", "r") as file:                                           # Read
    print(file.read())
    file.close()
