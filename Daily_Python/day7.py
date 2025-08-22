#Title: Palindrome Checker
#
#Difficulty: Beginner
#
#Challenge Description:
#Write a function that checks if a given string is a palindrome (a word or phrase that reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization).
#
#Constraints:
#
#Ignore spaces and punctuation.
#
#Ignore case differences.
#
#Input will be a single string.

user_input = input("Enter a palindrome: ")
cleaned = "".join(ch.lower() for ch in user_input if ch.isalnum())

if not cleaned:
    print(False)
elif cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)
