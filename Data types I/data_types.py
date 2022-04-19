# Data types

a = 5                                                                           # Numbers (int, float, and complex), strings, tuples, and
b = 72.4                                                                        # booleans are immutable, which means their contents can't
c = 1 + 3j                                                                      # be altered after creation
d = "String"
e = True                                                                        # True or False (capital 'T'/'F')
f = [1, "Hi", "Python", 2, (), {}]
g = (3, "Hey", "Andre", 4)
h = {"Batman", 12, "Superman"}

i = {                                                                           # Key : Value
    1: "John",
    2: "Paul",
    3: "George",
    4: "Ringo"
}

h = None

print(type(a))                                                                  # <class 'int'>
print(type(b))                                                                  # <class 'float'>
print(type(c))                                                                  # <class 'complex'>
print(type(d))                                                                  # <class 'str'>
print(type(e))                                                                  # <class 'bool'>
print(type(f))                                                                  # <class 'list'>
print(type(g))                                                                  # <class 'tuple'>
print(type(h))                                                                  # <class 'set'>
print(type(i))                                                                  # <class 'dict'>
print(type(h))                                                                  # <class 'NoneType'>

if h is None:
    h = "New value"
    print(h)
