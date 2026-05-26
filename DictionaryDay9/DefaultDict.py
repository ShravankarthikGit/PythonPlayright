##A defaultdict is a dictionary subclass that automatically initializes a default value the very
# first time you try to access or modify a missing key.

# When you create a defaultdict, you must hand it a factory function (like int, list, or set) in the parentheses.
# This function determines what the fallback value will be for any new key.

from collections import defaultdict

# Every new key automatically starts with []
student_classes = defaultdict(list)

# "Alex" doesn't exist yet, but Python creates [] and appends to it seamlessly
student_classes["Alex"].append("Math")
student_classes["Alex"].append("Science")

print(dict(student_classes))
# Output: {'Alex': ['Math', 'Science']}

# defaultdict with int
# Every new key automatically starts at 0
game_scores = defaultdict(int)

# "Player1" doesn't exist, so Python starts at 0 and adds 10
game_scores["Player1"] += 10

print(dict(game_scores))
# Output: {'Player1': 10}

# The Golden Rule of defaultdictSimply looking up or printing a missing key will permanently insert it into your dictionary
# with its default value.pythonfrom collections import defaultdict

inventory = defaultdict(list)

# Just checking a missing key...
print(inventory["shoes"])  # Output: []

# Look at the dictionary now; "shoes" has been officially added!
print(dict(inventory))     # Output: {'shoes': []}

### coding question
# Write a script that takes the following list of cities and groups them by their country using a defaultdict(list).
places = [
    ("USA", "New York"),
    ("UK", "London"),
    ("USA", "Chicago"),
    ("Japan", "Tokyo"),
    ("UK", "Manchester")
]

places_defaultdict = defaultdict(list)
for country,city in places:
    places_defaultdict[country].append(city)

print(dict(places_defaultdict))
# Output: {'USA': ['New York', 'Chicago'], 'UK': ['London']}