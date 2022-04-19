# List methods

dc_heroes = ["Superman", "Batman", "Flash", "Thor", "Aquaman"]

dc_heroes.append("Wonder-Woman")
dc_heroes.reverse()
dc_heroes.sort()
                                                                                # pop() removes the last item and returns it
marvel = dc_heroes.pop(4)                                                       # pop(index) removes the item from a specific position

dc_heroes.remove("Aquaman")                                                     # remove(value) removes an specific item based on its value
                                                                                # remove() returns 'None'
dc_heroes.extend(["Cyborg", "Green Lantern"])                                   # extend() allow us to add several items to a list
print(dc_heroes)
