# while

num = 1

while num < 10:
    print(num)
    num += 1


unconfirmed = ["John", "Bob", "Zack", "Carol"]
confirmed = []

while unconfirmed:
    confirmed.append(unconfirmed.pop())

confirmed.sort()
print(confirmed)
