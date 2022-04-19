# Lambda functions with map() and filter()

nums = [1, 5, 4, 6, 8, 11, 3, 12]

list_1 = list(map(lambda x: x * 2, nums))
print(list_1)

list_2 = list(filter(lambda x: (x % 2 == 0), nums))
print(list_2)
