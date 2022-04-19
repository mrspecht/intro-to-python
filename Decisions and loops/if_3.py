# if-else with logical operators

x = 5
if not x:                                                                       # The ‘not’ is a logical operator that will return True
    print("This is true")                                                       # if the expression is False
else:
    print("This is false")


string = ""                                                                     # Empty types (sequences, lists, tuples) and None are
if string:                                                                      # always evaluated False
    print("String has a value")

if not string:
    print("String does not have a value")
    print(bool(string))
