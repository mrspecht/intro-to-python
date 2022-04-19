# Reading a file

with open("heroes.txt", "r") as file:
    content = file.readline()                                                   # readline() method
    print(content)                                                              # Superman (plus an empty line)
    print(type(content))                                                        # String
    file.close()


with open("heroes.txt", "r") as file:                                           # readlines()
    content = file.readlines()
    print(content)                                                              # ['Superman\n', 'Batman\n'...]
    print(type(content))                                                        # List
    file.close()
