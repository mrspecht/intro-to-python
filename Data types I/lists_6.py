# List comprehensions

course = "Python essentials"

list_1 = []
for letter in course:                                                           # Traditional approach
    list_1.append(letter)


list_2 = [letter for letter in course]                                          # Modern approach. The first 'letter' is what we want to
print(list_2)                                                                   # return to our list


vowels = [letter for letter in course if letter.lower() in "aeiou"]             # Comprehensions
print(vowels)


numbers = [num for num in range(1, 10)]
print(numbers)


celsius = [-30, -20, -10, 0, 10, 20, 30]
fahrenheit = [int((temp * 1.8) + 32) for temp in celsius]
print(fahrenheit)
