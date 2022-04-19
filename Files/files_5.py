# Counting words and characters

import os.path

words = os.path.exists("words.txt")
count = 0

if words:
    try:
        with open("words.txt", "r") as file:
            lines = file.read().splitlines()
            word = max(lines, key=len)                                          # max() returns the largest item in an iterable or
                                                                                # the largest of two or more arguments
            for line in lines:
                count += 1
    finally:
        file.close()

    print(f"Words found: {count}")
    print(f"Longest word: {word}")
else:
    print("File not found")
