# Identifying exceptions

x = 13
y = 8

try:
    result = x + y + z
except Exception as e:
    print(e)                                                                    # Error message: name 'z' is not defined
    print(type(e))                                                              # Exception type: NameError
finally:
    print("Exception identified")
