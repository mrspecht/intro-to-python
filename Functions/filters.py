# Filters

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']                         # filter() constructs an iterator from elements of an
                                                                                # iterable for which a function returns true
def filter_letters(l):
    vowels = "aeiou"
    if l in vowels:
        return True
    else:
        return False


for letter in filter(filter_letters, letters):
    print(letter)


vowels = list(filter(filter_letters, letters))
print(vowels)
