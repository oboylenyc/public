#Difficulty: Beginner
#
#Challenge Description:
#Write a Python program that asks the user for a starting number and then counts down to 1 using a while loop. After reaching 1, print "Blast off!".
#
#Make sure your loop stops correctly and does not run forever.
#
#Assume the user enters a positive integer greater than 0.

n = int(input("Enter a positive number: "))

while n <= 0:
    n = int(input("Please enter a positive number: "))

while n > 0:
    print(n)
    n -= 1

print("Blast off!")