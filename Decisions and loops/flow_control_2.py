# Flow control (continue)

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 4]
count = 0

for l1 in list_1:
    for l2 in list_2:
        if l1 * l2 % 2 == 0:
            continue
        count += 1

print(count)
