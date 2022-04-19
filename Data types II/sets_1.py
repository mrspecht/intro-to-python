# Sets

countries = {"Canada", "Brazil", "India", "China"}                              # A set is an unordered collection that is iterable, mutable and
print(countries)                                                                # has no duplicate elements. A set itself may be modified, but
                                                                                # the elements contained in the set must be of an immutable type

pets = {"Cat", "Dog", "Rabbit", "Cat"}
pets.add("Otter")
print(pets)                                                                     # Prints one 'Cat' only

pets.remove("Cat")
print(pets)                                                                     # Removes 'Cat'


list = [1, 2, 2, 3, 4, 5, 5]
list_to_set = set(list)                                                         # Coverts a list to a set
print(type(list_to_set))
print(list_to_set)
