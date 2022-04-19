# Maps

nums = [2, 3, 7, 11, 14, 19]                                                    # map() applies a given function to each item of an iterable
                                                                                # and returns a list of the results
def power(n):
    if n > 10:
        n = n ** 2
    else:
        n = n ** 3

    return n


for num in map(power, nums):
    print(num)


num_list = list(map(power, nums))                                               # map(power, nums), by itself, returns its memory location
print(num_list)                                                                 # (<map object at 0x103604fd0>)
