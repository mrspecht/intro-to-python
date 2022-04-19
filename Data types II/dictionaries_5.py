# Dictionary comprehensions

keys = ["name", "age", "role", "course"]
values = ["Andre Specht", 38, "IT instructor", "Python"]
instructor_1 = {}

for key, value in zip(keys, values):                                            # Traditional approach
    instructor_1[key] = value


instructor_2 = {key:value for key, value in zip(keys, values)}                  # Comprehensions
print(instructor_2)


instructor_3 = {key:value for key, value in zip(keys, values) if key != "age"}
print(instructor_3)
