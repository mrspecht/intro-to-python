# Lambda functions

square = lambda num: num ** 2                                                   # In Python, an anonymous function is a function that is defined
result = square(5)                                                              # without a name. While normal functions are defined using the
print(result)                                                                   # 'def' keyword, anonymous functions are defined using the 'lambda'
                                                                                # keyword

add = lambda x, y: x + y                                                        # Syntax: lambda arguments: expression (it returns the expression)
print(add(7, 18))
