### Counter: Designed specifically for counting elements. Missing keys return 0 instead of raising an error.
# defaultdict: Automatically creates a default value (like an empty list or a zero) using a factory function when a missing key is accessed.
# OrderedDict: A dictionary subclass that remembers the exact insertion order of keys and includes order-specific methods like .move_to_end().
# ChainMap: Groups multiple independent dictionaries into a single lookup view. Searches them sequentially from left to right.
# UserDict: A wrapper around standard dictionaries designed specifically to be subclassed if you want to create your own custom dictionary type.


from collections import Counter

# Count occurrences of words in a list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words)
print(word_counts)
# Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
# Get the single most common item
print(word_counts.most_common(1))
# Output: [('apple', 3)]


counts = Counter({"apple": 2, "banana": 1})
# Missing keys safely return 0
print(counts["orange"])
# Output: 0
# Update the counter with new items
counts.update(["orange", "apple"])
print(counts)
# Output: Counter({'apple': 3, 'banana': 1, 'orange': 1})


inventory_store_A = Counter({'apples':5, 'bananas':3})
inventory_store_B = Counter(apples=2, bananas=8, oranges=4)

# Combine both inventories
total_inventory = inventory_store_A + inventory_store_B
print(total_inventory)
# Output: Counter({'bananas': 11, 'apples': 7, 'oranges': 4})

# Find the minimum shared stock (Intersection)
shared_stock = inventory_store_A & inventory_store_B
print(shared_stock)
# Output: Counter({'apples': 2, 'bananas': 3})




# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase (for example, "listen" and "silent").
def anagram_validator(String1, String2):

    # 1. Convert to lowercase and remove spaces
    clean_str1 = String1.lower().replace(" ", "")
    clean_str2 = String2.lower().replace(" ", "")

    counter1 = Counter(clean_str1)
    counter2 = Counter(clean_str2)

    if counter1 == counter2:
        return True
    else:
        return False

print(anagram_validator("apple", "banana"))
print(anagram_validator("silent", "listen"))

#  example 2
# Simulated log of IP addresses visiting a website
server_logs = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1",
    "172.16.0.4", "192.168.1.1", "10.0.0.5",
    "Unknown IP", "192.168.1.2", "Unknown IP"
]

traffic_counter = Counter(server_logs)
print(traffic_counter)

top_visitors = traffic_counter.most_common(1)
print(top_visitors)

# Remove 'Unknown IP' from our metrics entirely using 'del'
del traffic_counter["Unknown IP"]
print("Cleaned Log:", traffic_counter)

# Print value for non-existing key
print(traffic_counter['989.0098'])

# create counter on an empty list
fruits = Counter([]) ## we can also do Counter(list())
fruits['apple'] = 10
print(fruits)

