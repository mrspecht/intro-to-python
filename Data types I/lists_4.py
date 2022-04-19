# Slicing a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1 -> 9   0  1  2  3  4  5  6  7  8
# 1 <- 9  -9 -8 -7 -6 -5 -4 -3 -2 -1                                            # Slice syntax: [start:stop:step]

print(numbers[5:])                                                              # [6, 7, 8, 9]
print(numbers[1:4])                                                             # [2, 3, 4]
print(numbers[:6])                                                              # [1, 2, 3, 4, 5, 6]
print(numbers[:])                                                               # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::])                                                              # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[-7:-4])                                                           # [3, 4, 5]
print(numbers[:-5])                                                             # [1, 2, 3, 4]
print(numbers[-5:])                                                             # [5, 6, 7, 8, 9]
print(numbers[::-1])                                                            # [9, 8, 7, 6, 5, 4, 3, 2, 1]
