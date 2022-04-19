# Function with return

sentence = "anut fo raj a rof tun A"

def palindrome(sent):                                                           # Slice syntax: [start:stop:step]
    return sent[::-1]                                                           # We can use a negative step to obtain a reversed list


print(palindrome(sentence))
