# if-else statement

age = 23

if age >= 18:
    print("You can have a driver's license")
else:
    print("You are too young")


salary = 70_000

if salary < 40_000:
    print("Nah")
elif salary > 40_000 and salary < 60_000:                                       # No 'else if' in Python
    print("Okay")
else:
    print("Wow")
