# Flow control (break)

nums = [5, 4, 3, 2, 1, 0]
count = 0
result = 0

for num in nums:
    if num > 0:
        break
        count += 1

print(count)


for num in nums:
    if num > 0:
        result += 1
        break

print(result)
