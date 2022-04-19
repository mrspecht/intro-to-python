# Passing values by object reference

code = 111_222_333

def new_code(code):                                                             # In Python, values are passed to function by object reference.
    code = 444_555_666                                                          # If object is immutable than the modified value is not available
    return code                                                                 # outside the function. If object is mutable than modified value
                                                                                # is available outside the function
print(f"New code: {new_code(code)}")
print(f"Old code: {code}")


bills = ["Rent", "Hydro", "Internet", "Food"]

print(f"Bills to pay: {bills}")

def add_brand(bills):
    bills.clear()
    return bills
                                                                                # 'bills' is empty here
print(f"Bills to pay: {add_brand(bills)}")
