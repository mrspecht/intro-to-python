# Anagrams with a lambda function

import os.path

def anagrams(input):
    txt_file = os.path.isfile("words.txt")
    is_anagram = lambda w1, w2: sorted(w1) == sorted(w2)
    result = []

    if txt_file:
        try:
            with open("words.txt", "r") as file:
                lines = file.read().splitlines()
                for line in lines:
                    if is_anagram(input, line) and input != line:
                        result.append(line)
        finally:
            file.close()

        if result:
            for word in result:
                print(word)
        else:
            print(f"No results for '{input}'")
    else:
        print("File not found")


word = input("Enter an English word: ")
anagrams(word)
