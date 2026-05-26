# Multiplication Table: Print the multiplication table for a number entered by the user, up to 10.
# i = int(input("enter a numer:"))
# for j in range(1,11):
#     # print(j*i)
#     print(f"{i} x {j} = {j * i}")


# Print a Square: Take a number from the user and print a solid square of that size using a specific character, like *.
# i = int(input("enter a numer:"))
# for j in range(1,i+1):
#     print("*" * i)


# Sum of First 'n' Numbers: Get a number from the user and find the sum of all numbers from 1 up to that number.
# i = int(input("enter a numer:"))
# sum = 0
# for j in range(1,i+1):
#     sum = sum +j
# print(sum)


# Count Vowels in a Word: Ask the user for a word and count how many vowels are in it.
# i = input("enter a word:").lower()
# j = list(i)
# countofvowels=0
#
# for k in j:
#     if k in list("aeiou"):
#         countofvowels = countofvowels+1
# print(countofvowels)


# Fibonacci Sequence: Print the first 'n' terms of the Fibonacci sequence.
# i = int(input("enter a numer:"))
# a=0
# b=1
# for j in range(i):
#     print(a)        # Prints the current Fibonacci number
#     a, b = b, a + b # Instantly updates the variables for the next turn


# Input Validation with break: Repeatedly ask the user to enter a number between 1 and 10.
# Use a while loop and break to exit the loop only when a valid number is entered.

# while True:
#     i = int(input("enter a number between 1 and 10:"))
#     if (1<=i<=10):
#         break
#     print("Invalid choice. Try again.")


# Skip Multiples with continue: Print all numbers from 1 to 20, but skip the numbers that are multiples of 3 using the continue statement.
# for i in range(1,21):
#     if(i%3 == 0):
#         continue
#     print(i)



# Count 'a's and 'b's in a word: Get a word from the user. Iterate through the word and count the occurrences of the letter
# 'a' and 'b', using continue to skip any other letters.

i = input("Enter a word:")

countA = 0
countB = 0
for j in i:
    if (j == 'a'):
        countA += 1
    elif (j == 'b'):
        countB += 1
    else:
        continue
print(f"count of 'a' is {countA}")
print(f"count of 'b' is {countB}")

