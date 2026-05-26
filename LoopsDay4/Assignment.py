# if, if-else, and if-elif-else
# 1.
# Positive, Negative, or Zero: Get a number from the user and print whether it's positive, negative, or zero.
# 2.
# Vowel or Consonant: Take a single letter as input and check if it's a vowel (a, e, i, o, u) or a consonant.
# 3.
# Grading System: Get a student's score (0-100) and assign a letter grade (A, B, C, D, or F) based on a simple scale.

# Positive, Negative, or Zero: Get a number from the user and print whether it's positive, negative, or zero.
# i = int(input("input a number:"))
# print(i)
#
# if(i>0):
#     print ("number is positive")
# elif(i<0):
#     print("number is negative")
# else:
#     print("number is 0")


# Vowel or Consonant: Take a single letter as input and check if it's a vowel (a, e, i, o, u) or a consonant.
# j = input("input a character:")
#
# if j in ['a','e','i','o','u']:
#     print(f"{j} is a vowel")
# else:
#     print(f"{j} is a Consonant")

# Grading System: Get a student's score (0-100) and assign a letter grade (A, B, C, D, or F) based on a simple scale.
# k = float(input("input a score:"))
# print(k)
#
# if(k>=90.00):
#     print("Student grade is A")
# elif(70.00<=k<90.00):
#     print("Student grade is B")
# elif(50.00<=k<70.00):
#     print("Student grade is C")
# elif(35.00<=k<50.00):
#     print("Student grade is D")
# else:
#     print("Student grade is F")



# while loop

# Sum of Digits: Get a number and calculate the sum of its digits using a while loop. For example, for the number 123, the sum is 1+2+3=6.
# i = int(input("enter a number more than 1 digit:"))
# j = list(str(i))
# sum = 0
# k=0
# while k<len(j):
#     sum = sum + int(j[k])
#     k+=1
# print(sum)

#  approach Two
# num = int(input("enter a number more than 1 digit: "))
# digit_sum = 0
#
# while num > 0:
#     remainder = num % 10  # Grabs the very last digit (e.g., 123 % 10 = 3)
#     digit_sum = digit_sum + remainder  # Adds that digit to the running total
#     num = num // 10  # Chops off the last digit (e.g., 123 // 10 = 12)
#
# print(f"The sum of the digits is: {digit_sum}")

# Reverse a Number: Take a number and print its reverse. For example, reversing 1234 gives 4321

i = int(input("enter a number more than 1 digit:"))
j = list(str(i))

k = len(j)
reverseNum=""
while k>0:
    reverseNum = reverseNum + j[k-1]
    k-=1

print(reverseNum)

# Approach 2
i = int(input("enter a number more than 1 digit: "))
reverseNum = str(i)[::-1]  # The [::-1] instantly reverses the string
print(reverseNum)


# Mathematical way
num = int(input("enter a number more than 1 digit: "))
reverseNum = 0

while num > 0:
    remainder = num % 10
    reverseNum = (reverseNum * 10) + remainder
    num = num // 10

print(reverseNum)













