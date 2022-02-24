# ---------------------- Importing the modules in ur program
# ----------1 . Generic import
import random
print(random.randint(1, 10))

# ----------2 . Specific function from module
from random import randint
print(randint(1, 10))

# ----------3 . Universal import
from random import *
print(randint(1, 10))
