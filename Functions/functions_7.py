# Preventing a function from modifying a list

unconfirmed = ["John", "Bob", "Zack", "Carol"]
confirmed = []

def mod_list(unconfirmed, confirmed):
    while unconfirmed:
        confirmed.append(unconfirmed.pop())
    confirmed.sort()

mod_list(unconfirmed, confirmed)
print(unconfirmed)
print(confirmed)


to_print = ["Assignment", "Project", "Python cheat sheet"]
printed = []

mod_list(to_print[:], printed)                                                  # The slice notation ([:]) makes a copy of the list
print(to_print)
print(printed)
