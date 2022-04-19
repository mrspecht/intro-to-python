# Flow control (break)

films = ["Terminator 2", "MIB", "JFK", "Forrest Gump"]

for film in films:
    if film == "JFK":                                                           # 'break' is a statement that causes the control flow to exit
        break                                                                   # the loop structure and returns control to the enclosing
    print(film)                                                                 # statement


while True:
    name = input("Guess my name: ")
    if name.lower() == "andre":
        print("Congrats. You win")
        break
    else:
        print("Try again")
