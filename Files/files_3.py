# Reading a file

with open("heroes.txt", "r") as file:
    content = file.read()                                                       # read() method
    print(content.rstrip())                                                     # Same output (string) as seen in the file
    print(type(content))                                                        # rstrip() removes any whitespace characters from the
    file.close()                                                                # right side of a string


with open("heroes.txt", "r") as file:                                           # read() + splitlines()
    content = file.read().splitlines()
    print(content)                                                              # ['Superman', 'Batman'...]
    print(type(content))                                                        # List
    file.close()
