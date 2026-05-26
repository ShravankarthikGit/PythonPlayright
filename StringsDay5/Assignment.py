# i = 'apple'
# j = "banana"
# k = str("kiwi")
#
# print(i,j,k)
# print(type(i))
# print(type(j))
# print(type(k))

# str = "hello"
# print(id(str))
# str2 = str+"world"
# print(id(str2))

# print("python" + "rocks")
# print("python"*3)

# text="welcome"
# print(text[1:4])
# print(text[:5])
# print(text[-3:])

# print lco
# print(text[2:5])

######Check Substring using in and not in
# Task: Write a program that asks the user to input a word. Check if "python" is present in that word. Print "Found" or "Not Found".

# text = input("input a word:")
# if "python" in text:
#     print("Found")
# else:
#     print("Not found")

# Task: Take user input for name and age. Use an f-string to print: "My name is <name>, and I am <age> years old."
# name = input("input a name:")
# age = input("input age:")
# print(f"My name is {name}, and I am {age} years old.")

# Write a program that takes "welcome to python" and prints:
# Capitalized string
# Title case string
# Uppercase string
# Swapcase string

# text="welcome to python"
#
# print(text.upper())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())

# Given string "banana", count how many times "a" appears. Then replace "banana" with "orange" in the string "I like banana".

# fruit = "banana"
# print(fruit.count("a"))
#
# str = "I like banana"
# print(str.replace("banana","orange"))

# Ask the user to input a string. Check if:
# It contains only alphabets (isalpha())
# It contains only digits (isdigit())
# It is alphanumeric (isalnum()) Print results accordingly.

# input = input("input a word:")
# print(input.isalpha())
# print(input.isdigit())
# num = "2424.24234"
# print(num.isnumeric())
# print(input.isalnum())


# Given string " apple,banana,grape ", strip spaces.
# Split the string by commas ,.
# Print the list of fruits.

text=" apple,banana,grape "
text = text.strip()
list = text.split(",")
print(list)

fruits_list = text.strip().split(",")
print(fruits_list)














