# new_list = [expression for item in iterable]

# def check_even_numer(var: list):
#     result = [num for num in var if num % 2 == 0]
#     print(result)
#
# check_even_numer([1,2,3,4,5])

# If you want to DROP items from the list: Put a single if at the END.
# If you want to KEEP ALL items but change their look: Put the if / else at the FRONT.

# def capitalize_words(words: list):
#     caps =[res.upper() for res in words ]
#     print(caps)
#
# capitalize_words(["apple", "banana", "orange"])
#
#
# def check_even_odd(lst: list):
#     result = ["Even" if num%2 else "odd" for num in lst]
#     print(result)
#
# check_even_odd([1,2,3,4,5])

# If a price is greater than 100, subtract 10 from it (a discount).
# If it is 100 or less, leave it exactly as it is.

# def validate_num(var: list):
#     result = [ num-10 if num > 100 else num for num in var]
#     print(result)
#
# validate_num([120,22,33,498,105])

# Imagine you are given a list of user dictionaries from a database.
# You need to write a function that extracts the names of all users, but only if they are active.

# users = [
#     {"name": "Alex", "age": 28, "is_active": True},
#     {"name": "Bob", "age": 34, "is_active": False},
#     {"name": "Charlie", "age": 22, "is_active": True},
# ]

# using conventional for loop
# def exract_data_dictionaries(dic_list: list):
#     for dic in dic_list:
#         if dic.get("is_active") == True:
#             print(dic.get("name"))


# using list comprehension
# def exract_data_dictionaries(dic_list: list):
#     result = [dic.get("name") for dic in dic_list if dic.get("is_active") == True]
#     print(result)

    # for dic in dic_list:
    #     if dic.get("is_active") == True:
    #         print(dic.get("name"))

# exract_data_dictionaries(users)

#conventional for loop to sum up all the even numbers in a list?

# def sum_all_even_numbers(lst: list):
    # sum = 0
    # for num in lst:
    #     if num % 2 == 0:
    #         sum += num
    # print(sum)
    # using list comprehension
#     print(sum([num for num in lst if num % 2 == 0]))
#
# sum_all_even_numbers([3,8,6,4,0])

# while loop to reverse a number

# def rev_num_while(num: int):
#     num_str = str(num)
    # num_list = list(num_str)
    # i = 0
    # rev_num_list = []
    # while i < len(num_list):
    #     target_index = -1 - i
    #     rev_num_list.append(num_list[target_index])
    #     i += 1
    # final_num = int("".join(rev_num_list))

    # pythonic way to reverse
#     final_num = num_str[::-1]
#     print(final_num)
#
# rev_num_while(23236)

# Given two lists of numbers, return a new list containing only the numbers that appear in both lists.
# Each number in the final output must be unique.

# def unique_list(list_one: list, list_two: list):
#     set_one = set(list_one)
#     set_two = set(list_two)
#
#     common_set = set_one & set_two
#     common_items = set_one.intersection(set_two)
#     print(common_items)
#     # we can use sorted to sort a set
#     print(sorted(common_set))
#
# unique_list([2,7,8,9,10],[2,3,7,9,10,18])


# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
def recurring_integer(list_one: list, k: int):
    # So i will create a dictionary with item which contains
    # key as number and value as count of repetition
    count = {}
    for num in list_one:
        if num in count:
            # we increment the value of num by 1 in case present
            count[num] += 1
        else:
            count[num] = 1

    result = []
    # Clean lookup using .items() unpacking
    for key, value in count.items():
        if value >= k:
            result.append(key)
    print(result)
    return result


recurring_integer([1,2,3,3,3,4,4,5,6,6,6], 2)













