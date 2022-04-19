# Handling exceptions

x = 15                                                                          # An exception is an event that occurs during the
y = 0                                                                           # execution of a program that disrupts the normal flow
result = 0                                                                      # of instructions

try:
    result = int(x / y)
except ZeroDivisionError:                                                       # Exceptions are classes
    result = "N/A"
finally:
    print("Result is", result)                                                  # The 'finally' block always executes when the 'try'
                                                                                # block exits
