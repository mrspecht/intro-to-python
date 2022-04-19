# Args & kwargs

def order(name, *dishes, **info):                                               # We use '*args' and '**kwargs' as an argument when we
    print(f"Hello {name}")                                                      # are unsure about the number of arguments to pass in
    print("\nWe are delivering the following items:")                           # the functions
    for index, dish in enumerate(dishes):
        print(f"{index + 1}: {dish}")
    if (info.get("recipient")):
        address = info.get("recipient")
        print(f"\nTo the address: {address}")


order(
    "John Hungry",
    "Large deluxe pizza",
    "Chow mein",
    "Coca-Cola 2L",
    recipient="123-500 Big Ave"
)
