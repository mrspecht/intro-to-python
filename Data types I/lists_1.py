# Lists

fruits = ["orange", "guava", "banana", "tomato"]                                # Indexes (left to right):  0,  1,  2,  3
                                                                                # Indexes (right to left): -4, -3, -2, -1
for fruit in fruits:
    print(fruit)


print(f"Length: {len(fruits)} items")                                           # Proper way to concatenate different types of variables

print(fruits[0])                                                                # orange
print(fruits[3])                                                                # tomato
print(fruits[-1])                                                               # tomato
print(fruits[-3])                                                               # guava
# print(fruits[-5])                                                             # Index out of range
