# Concatenating strings (f-strings)

import datetime

msg = "Hello"                                                                   # Python does not do implicit string conversion
# new_msg = msg + 2                                                             # Error message


name = "Eric"
age = 45
message = f"Hello, {name}. You are {age}"                                       # Literal string interpolation (f-strings)
print(message)                                                                  # print("Your age is " + age) doesn't work


num_1 = 12
num_2 = 23
message = f"{num_1} + {num_2}"
print(message)                                                                  # 12 + 34


today = datetime.datetime.today()                                               # Print today's date using the datetime library
print(f"{today:%B %d, %Y}")
