# Zipping iterables

letters = ['a', 'b', 'c', 'd']                                                  # The zip() function takes iterables (can be zero or more),
numbers = [1, 2, 3, 4]                                                          # aggregates them in a tuple, and return it

result = list(zip(letters, numbers))                                            # Casting the result as a list, otherwise the result would be
print(result)                                                                   # <zip object at 0x10f7d6b40>


for letter, number in zip(letters, numbers):
    print(f"{letter} is {number}")
