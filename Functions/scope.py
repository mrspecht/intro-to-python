# Scope

language = "Java"                                                               # In Python, (almost) everything is an object. What we commonly
                                                                                # refer to as 'variables' in Python are more properly called
def new_lang():                                                                 # 'names'. Likewise, 'assignment' is really the binding of a name
    language = "Python"                                                         # to an object. Each binding has a scope that defines its
    return language                                                             # visibility, usually the block in which the name originates

print(new_lang())
print(language)


country = "Canada"

def set_country():
    country = "India"

    def new_country():
        country = "Brazil"
        print(country)

    new_country()
    return country

print(set_country())
print(country)
