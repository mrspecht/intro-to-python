# Indentation

def func_1():                                                                   # Most of the programming languages use braces to define
    message = "Hello world"                                                     # a block of code. Python, however, uses indentation
                                                                                # PEP8 recommends 4 spaces per indentation level
    print("Hey Python")


def func_2():
    message = "Hello world"

print("Are you a snake?")                                                       # Instruction outside the 'func_2' block


test = "indentation"
    print(test)                                                                 # IndentationError: unexpected indent
