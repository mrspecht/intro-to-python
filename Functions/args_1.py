# Args & kwargs

def my_args(*args):                                                             # In Python, we can pass a variable number of arguments to
    for arg in args:                                                            # a function using special symbols, '*args' (arguments) and
        print(arg)                                                              # '**kwargs' (keyword arguments)
    print(type(args))                                                           # 'args' returns a tuple

my_args(1, 2, 3, "Hello", ["Pyton", "Java"])


def my_kwargs(**kwargs):
    for key, value in kwargs.items():                                           # 'kwargs' returns a dictionary (key-value pairs)
        print(f"Key: {key.title()} \t Value: {value}")
    print(type(kwargs))

my_kwargs(name="Andre", age=38, course="Python")                                # No spaces should be used on either side of the equal sign
