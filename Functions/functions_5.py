# Function with a default value

def set_salary(salary=40_000):                                                  # No spaces should be used on either side of the equal sign
    print("Your salary is", salary)

set_salary()
set_salary(55_000)


def full_name(first, last, middle=""):                                          # A default (optional) value must be the last parameter in
    pass                                                                        # the parameter list
