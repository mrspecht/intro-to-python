# Anagrams

import os.path

def gen_key(word):
    key = ''.join(sorted(word))
    return key


def anagrams(input):
    txt_file = os.path.exists("words.txt")
    word = gen_key(input)
    result = []

    if txt_file:
        try:
            with open("words.txt", "r") as file:
                lines = file.read().splitlines()
                for line in lines:
                    keyword = gen_key(line)
                    if word == keyword and input != line:
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
