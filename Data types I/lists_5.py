# Lists (useful functions)

from random import shuffle                                                      # Imports shuffle() from the 'random' package

numbers = [1, 12, 23, 30, 44]

print(min(numbers))                                                             # min() returns the smallest item in an iterable
print(max(numbers))                                                             # max() returns the largest item in an iterable
print(sum(numbers))


names = ["Andre", "John", "Bob", "Alfred"]

print(min(names))                                                               # Alfred (based on an alphabetical order)
print(max(names))                                                               # John


message = ["Python", "is", "amazing"]
string = ' '.join(message)
print(string)                                                                   # 'Python is amazing'

new_list = string.split(' ')
print(new_list)                                                                 # ['Python', 'is', 'amazing']


shuffle(message)
print(message)
