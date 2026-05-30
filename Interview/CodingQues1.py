def count_frequencies(words: list[str]) -> dict[str, int]:
    freq_map = {}

    for word in words:
        # If word isn't there, .get() returns 0. Then we add 1.
        freq_map[word] = freq_map.get(word, 0) + 1

    return freq_map


# Example usage:
word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(count_frequencies(word_list))
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

# The  slice notation. is used to reverse the string
# sequence[start : stop : step]
# rev_string = var[ :: -1]
# #                │ │  └─ Step is -1 (Move backward 1 item at a time)
# #                │ └──── Stop is blank (Go all the way to the beginning)
# #                └────── Start is blank (Begin at the very end of the string)


def string_rev(var: str):
    rev_string = var[:: -1]
    print(rev_string)
string_rev("banana")


def extract_every_second_character_string(var: str):
    # python will perform looping for the string output from slice 
    sec_lst= list(var[0::2])
    print(sec_lst)





extract_every_second_character_string("willow")
