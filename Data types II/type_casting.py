# Type casting (explicit type conversion)

age = "30"
age = int(age)
print(type(age))


tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
st = set(tpl)
print(type(lst))
print(type(st))


lang = "Python"
has_lang = bool(lang)
print(type(has_lang))


food = {
    "Option 1": "Lasagna",
    "Option 2": "Pasta",
    "Option 3": "Pizza"
}

print(type(food.items()))                                                       # <class 'dict_items'>
print(type(list(food.items())))
print(type(tuple(food.items())))
