#Title: Even or Odd Checker
#
#Difficulty: Beginner
#
#Challenge Description:
#Write a Python program that asks the user for an integer and prints whether the number is even or odd.
#
#Use the modulo operator (%) to check divisibility.
#
#Make sure your program handles both positive and negative integers correctly.

uinput = float(input("Enter a number: "))

if uinput.is_integer(): 
    num = int(uinput)
    if num == 0:
        print("Zero is neither even nor odd")
    elif num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Not an integer, cannot be even/odd")