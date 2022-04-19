# Tuples

fruits = ("orange", "guava", "banana", "tomato")                                # A tuple is similar to a list, but it is immutable

for fruit in fruits:
    print(fruit.title())


print(fruits.count("banana"))


correct_list = fruits[0:3]
print(correct_list)

del fruits
