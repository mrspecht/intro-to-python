# String methods

name = "bRuCe WaYnE"
title = "Batman, The Dark Knight"
                                                                                # Slice operator (work with sequences)
print(title[0:6])                                                               # Batman
print(title[6])                                                                 # ,
print(title[12:16] * 4)                                                         # DarkDarkDarkDark

print(len(name))                                                                # 11


print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.startswith('C'))
print(name.endswith('e'))                                                       # False (case sensitive)
print(title.count('a'))
