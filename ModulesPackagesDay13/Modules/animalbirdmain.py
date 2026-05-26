# --- Approach 1: Importing with module names ---
import animal
import bird

animal.fly()     # Calls fly() from animal module
animal.color()   # Calls color() from animal module

bird.fly()       # Calls fly() from bird module
bird.color()     # Calls color() from bird module


# ---- Approach 2: Importing everything (*) -----
from animal import *
fly()    # Calls animal.fly()
color()  # Calls animal.color()

from bird import *
fly()    # Now fly() from bird overrides the previous one
color()  # Calls bird.color()

fly()    # Always refers to latest imported fly() i.e. bird.fly()