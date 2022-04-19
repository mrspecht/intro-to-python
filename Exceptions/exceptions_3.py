# Handling exceptions

x = 15
y = 3
result = 0

try:                                                                            # 'try' block with an 'else'
    result = int(x / y)
except ZeroDivisionError:
    result = "N/A"
else:                                                                           # The 'else' block is executed if the 'try' clause
    print("The divisor is not zero")                                            # does not raise an exception
finally:
    print("Result is", result)
