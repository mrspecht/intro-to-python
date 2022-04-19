# Identity operators

x = 10
y = x

print(id(x))                                                                    # id() returns the object's memory address
print(id(y))

print(x is y)                                                                   # The 'is' keyword is used to test if two variables refer
print(x is not y)                                                               # to the same object
