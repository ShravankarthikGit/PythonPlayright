

import operations


operations.add(10, 20)   # Access using module name
operations.mul(10, 20)

# Access dictionary variable from module
a = operations.person1["age"]
print(a)


# ---------------- Approach 2: Importing specific functions ----------------
from operations import add, mul
add(10, 20)
mul(10, 20)


# ---------------- Approach 3: Importing everything (*) ----------------
from operations import *
add(10, 20)
mul(10, 20)