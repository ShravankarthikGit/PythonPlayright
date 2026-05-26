
#capitalize()	Converts the first character to upper case
# s="hello"
# print(s.capitalize())  #Hello


#casefold()	and lower(): Converts string into lower case
s="Hello"
# .casefold() when you need to match or compare strings in a case-insensitive way, especially if your program handles
# international text or special characters from other languages.
print(s.casefold()) #
print(s.lower()) #hello

#upper() : Converts sting to upper case
s="Hello"
print(s.upper()) #HELLO

# title()	Converts the first character of each word to upper case
s="welcome to python"
print(s.title()) #Welcome To Python

# swapcase()	Swaps cases, lower case becomes upper case and vice versa

s="Welcome To Python"
print(s.swapcase()) # wELCOME tO pYTHON


#center() : Returns a centered string
str="banana"
print(str.center(10))
print(str.center(10,'*')) #**banana**

#format()	Formats specified values in a string
name="John"
print("Hello {}".format(name))  # Hello John


#find()	Searches the string for a specified value and returns the position of where it was found
s="hello"
print(s.find("e"))  # 1
print(s.find("l"))  # 2
print(s.find("x"))  # -1   value is not found

# index()	Searches the string for a specified value and returns the position of where it was found
# Same as find(), but raises a ValueError if the value is not found.

print(s.index("e"))
print(s.index("l"))
#print(s.index("x"))  #ValueError:

#count()	Returns the number of times a specified value occurs in a string
s="banana"
print(s.count("a")) #3
print(s.count("na")) #2

# replace()	Returns a string where a specified value is replaced with a specified value
s="Hello world"
print(s.replace("world", "There")) #Hello There
print(s.replace("l","X")) #HeXXo worXd


#isalnum()	Returns True if all characters in the string are alphanumeric (no punctuation or spaces or no special chars).

s="ABC123"
print(s.isalnum()) #True

s="abc!"
print(s.isalnum()) #False


#isalpha()	Returns True if all characters in the string are in the alphabet
s="Hello"
print(s.isalpha()) # True

s="123"
print(s.isalpha()) #False

#isdecimal()	Returns True if all the characters are decimals (0-9).

s="123"
print(s.isdecimal()) #True
s="123.55"
print(s.isdecimal()) #False
s="xyz"
print(s.isdecimal()) #False


# isdigit() Returns True if all the characters are digits, otherwise False.

s="123"
print(s.isdigit()) #True

s="xyz"
print(s.isdigit()) #False

s="12.5"
print(s.isdigit()) #False

#isnumeric() Returns True if all the characters are numeric (0-9), otherwise False.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric,
# and the - and the . are not.

s="123"
print(s.isnumeric()) #True

s="xyz"
print(s.isnumeric()) #False

s="12.5"
print(s.isnumeric()) #False


#isLower()
#isUpper()

s="welcome"
print(s.islower()) #True
print(s.isupper()) #False



















