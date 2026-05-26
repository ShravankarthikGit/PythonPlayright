## creating strings in 3 appraoches

# Approach1 : using double quotes
# name="John"
# grade="B"

# Appraoch2: using single quotation
# name='John'
# grade='B'

#Approach3 : Using constructor

# name=str()   # empty string
# grade=str()  # empty string
# print(name, grade)
#
# name=str("John")
# grade=str("B")

# print(name, grade)
# #
# print(type(name))
# print(type(grade))

## +   and  * operators with strings
# str="welcome"
# print(str+" Programming")
# print(str * 3)


## Slicing strings
# starting index count from 0
# ending index count from 1

# mystr="welcome"
#
# print(mystr[1:3])  # el
# print(mystr[:6])  # welcom #here starting index is 0 by default
# print(mystr[2:]) #lcome    # here ending index is last value
#
# mystr="welcome"
# # when we give negative index it will count from end
# print(mystr[1:-1])  #elcom
# print(mystr[1:-2]) # elco
# print(mystr[-5:-2]) #lco


## Formating strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string,
# simply put an 'f' in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Example 1
# age=30
#str="My name is John, Im am "+age   # TypeError:

# str= f"My name is John, Im am {age}"
# print(str)   #print(f"My name is John, Im am {age}")

#Example 2:
# Output: The price is 55.00

# price=55
# price: The name of your variable containing a number.
# :: Signals the start of the formatting rules.
# .2: Specifies the precision to exactly two decimal places (it rounds the number automatically).
# f: Specifies the type as a Fixed-point float (a decimal number).

# str=f"The price is {price:.2f} "
# print(str)

#Example 3:
# price=20
# str=f"The price is {price * 10} dollards"
# print(str)


# in  notin  with strings
# returns the boolean value

# str="welcome"
# print("come" in str)  # True
# print("lome" in str)  # False
#
# print("come" not in str)  # False
# print("lome" not in str)  # True













