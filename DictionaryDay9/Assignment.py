## Write a function count_letters(text) that takes a string and returns a standard dictionary with the count of each letter.
# Do not ignore spaces or change the case for this one.

from collections import Counter

def count_letters(text):
    ctr = Counter(text)
    return ctr
print(count_letters("apple"))

# Approach 2
def count_letters(text):
    #  create a dictionary
    dict = {}
    # loop through text and add items to dictionary
    for i in text:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict
print(count_letters("apple"))


# Write a function group_by_length(words) that takes a list of strings and groups them into a dictionary
# where the keys are word lengths (integers) and the values are lists of words with that length.

# Input: ["cat", "dog", "apple", "bird"]

def count_by_length(words):
    output = {}
    for word in words:
        if word not in output:
            output[word] = len(word)

    return output

print(count_by_length(["cat", "dog", "apple", "bird"]))
# output: {'cat': 3, 'dog': 3, 'apple': 5, 'bird': 4}


### output be like::::   {3: ['cat', 'dog'], 5: ['apple'], 4: ['bird']}
def group_by_length(words):
    output = {}
    for word in words:
        length = len(word)
        if length not in output:
            output[length] = []

        output[length].append(word)

    return output

print(group_by_length(["cat", "dog", "apple", "bird"]))


###### Write a function calculate_total(cart, prices) that takes a shopping cart dictionary (item names as keys,
# quantities as values) and a prices dictionary. Return the total cost of all items in the cart.

my_cart = {"apple": 3, "banana": 2}
my_prices = {"apple": 0.50, "banana": 0.25, "orange": 0.75}

def calculate_total(cart, prices):
    total = 0
    for key, value in cart.items():
        # Look up the price directly using the key
        item_price = prices[key]
        # Use += to add it to the running total (don't overwrite it!)
        total += value * item_price
    return total

print(calculate_total(my_cart, my_prices))


# Challenge 1: Remove Duplicates Keep Order (List + Set)
song_list = ["Song A", "Song B", "Song A", "Song C", "Song B"]

seen = set()          # Used to track duplicates fast
final_song_list = []  # Used to keep the clean songs in order

for song in song_list:
    if song not in seen:
        final_song_list.append(song)
        seen.add(song)  # Remember that we saw this song

print(final_song_list)

# Write a function extract_unique_tags(sentence) that finds all words starting with a hashtag # in a sentence.
# Return a set of these tags in lowercase, with the # symbol removed.
#  Input: "Coding in #Python is fun. I love #python and #AI"

def extract_unique_tags(sentence):
    unique_tags = set()
    # 1. Split the sentence into individual words
    words = sentence.split()
    for word in words:
        if word.startswith("#"):
            cleaned_tag = word.lower().strip("#.,!?")
            unique_tags.add(cleaned_tag)
    return unique_tags
print(extract_unique_tags("Coding in #Python is fun. I love #python and #AI"))


# You are given a list of tuples containing student names and their exam scores. Write a function build_grade_book(scores_list)
# that groups all scores into a dictionary where the student('s name is the key and the value is a list of all their scores.'

# Input: [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 80)]
# Expected Output: {')Alice': [85, 95], 'Bob': [90, 80]}

def build_grade_book(scores_list):
    dict = {}
    for name, score in scores_list:
        if name not in dict:
            dict[name] = [score]
        else:
            dict[name].append(score)
    return dict

data = [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 80)]
print(build_grade_book(data))

# You have a dictionary representing people and their lists of friends.
# Write a function common_friends(network, person1, person2) that returns a set of mutual friends shared between person1 and person2.
# Input Network: {"Alice": ["Bob", "Charlie", "David"], "David": ["Alice", "Charlie", "Eve"]}
# Target People: "Alice", "David"Expected
# Output: {'Charlie'} (Since Charlie is the only one in both lists)

def common_friends(network, person1, person2):
    person1_friends = set(network[person1])
    person2_friends = set(network[person2])
    common_friends = person1_friends & person2_friends
    return common_friends

friends_network = {
    "Alice": ["Bob", "Charlie", "David"],
    "David": ["Alice", "Charlie", "Eve"]
}
print(common_friends(friends_network, "Alice", "David"))




