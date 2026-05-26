# ---- Approach 1: Importing full modules ------
import classA
import classB

obj1 = classA.Animal()
obj1.display()   # Output: I like Cow

obj2 = classB.Bird()
obj2.display()   # Output: I like Parrot



# ---- Approach 2: Importing specific classes ------
from classA import Animal
from classB import Bird

obj3 = Animal()
obj3.display()   # Output: I like Cow

obj4 = Bird()
obj4.display()   # Output: I like Parrot