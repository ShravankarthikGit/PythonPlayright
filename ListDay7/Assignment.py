# Ask the user to input 5 numbers one by one and store them in a list. Write a loop to find and print the
# largest number in that list without using the built-in max() function.

# newlist = []
# for i in range(5):
#     x = int(input("enter a numer:"))
#     newlist.append(x)
# print(newlist)
# largestNum = newlist[0]
# for k in newlist:
#     if k>largestNum:
#         largestNum=k
# print(largestNum)

# Given the starting list numbers = [12, 5, 8, 19, 22, 3, 14], write a program that loops through it and creates
# a brand-new list containing only the even numbers. Print your new list at the end.

# numbers = [12, 5, 8, 19, 22, 3, 14]
# evenlist =[]
# for i in numbers:
#     if i%2==0:
#         evenlist.append(i)
# print(evenlist)


# Given a list with repeated items fruits = ["apple", "banana", "apple", "grape", "banana"],
# write a loop that removes all duplicate entries and keeps only unique values.

# fruits = ["apple", "banana", "apple", "grape", "banana"]
# uniquefruits = []
# for i in fruits:
#     if i not in uniquefruits:
#         uniquefruits.append(i)
# print(uniquefruits)
#
# #### Approach 2
# # Convert to a set to remove duplicates, then back to a list
# uniquefruits = list(set(fruits))
# print(uniquefruits)

####Write a loop that checks both lists and builds a brand-new list containing only the numbers that appear in both lists.

# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
#
# set_a = set(list_a)
# set_b = set(list_b)
#
# set_common = set_a.intersection(set_b)
# print(set_common)
#
# #### With for loop
# common_list = []
# for item in list_a:
#     if item in list_b:
#         common_list.append(item)
# print(common_list)  # Outputs: [4, 5]

#### Reverse Words in a Sentence

# text = "Hello World Python"
# li = list(text.split(" "))
# print(li)
# li.reverse()
# print(li)

### approach 2
# text = "Hello World Python"
# li = list(text.split(" "))
# revlist = li[::-1]
# print(revlist)


#####Separate Odd and Even Numbers
mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []
odd_numbers = []

for i in mixed_numbers:
    if i%2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)





