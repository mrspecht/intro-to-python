# Function with docstrings

x = 10
y = 15
z = 30

def is_even(num):
    """Function to check if the number is even or odd"""

    if (num % 2) == 0:
        print(f"Number {num} is even")
    else:
        print(f"Number {num} is odd")


print(is_even.__doc__)
help(is_even)
