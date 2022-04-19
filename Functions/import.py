# Importing functions from a module

from module import signup                                                       # 'from module import *' would be the proper way to
from module import password                                                     # import all classes at same time

name = "Andre Specht"                                                           # Python creates a folder called '__pycache__' when we
age = 38                                                                        # run this code
username = "andrespecht"
                                                                                # Modules and functions can have aliases
signup(name, age, username)

pwd = password(username)
print(pwd)
