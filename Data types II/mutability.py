# Mutable vs immutable

a = "Winnipeg"
b = a

print(id(a) == id(b))                                                           # The == operator compares the values of two objects
print(a is b)                                                                   # The 'is' operator compares the identity of two objects

shopping_list = ["bread", "orange juice", "eggs"]
shopping_list.append("apple pie")                                               # Lists are mutable
print(shopping_list)

heroes = "The Avengers"
print(id(heroes))

heroes = "Justice League"                                                       # Creates a new variable with the name 'heroes'
print(id(heroes))                                                               # Strings are immutable
