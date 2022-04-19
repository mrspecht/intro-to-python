from time import sleep

dots = ['', '.', '..', '...']
cond = True
i = 0

while cond:
    sleep(.75)
    print(f"Loading{dots[i % 4]}".ljust(10), end='\r', flush=True)

    if i < 4:
        i += 1
    else:
        i = 1
