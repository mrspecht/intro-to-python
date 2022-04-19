# for loops (index)

brands = ["Samsung", "Apple", "Microsoft", "Xiaomi", "Dell"]

for i in range(len(brands)):                                                    # Iterates through the list's length (from 0 to 4)
    print(f"{i}: {brands[i]}")

for index, brand in enumerate(brands):                                          # Using the enumerate() function. enumerate() adds counter to
    print(f"{index}: {brand}")                                                  # an iterable and returns it (the enumerate object)


sep = "\n------------\n"

for index, brand in enumerate(brands):
    print(f"{index + 1}: {brand}", end = sep)
