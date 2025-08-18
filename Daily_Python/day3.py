#Write a Python program that asks the user for a positive integer n. Your program should then print all the numbers from 1 to n, but:
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz".
#For multiples of both 3 and 5, print "FizzBuzz".
#Constraints:
#Assume the user always enters a positive integer.
#Output each result on a new line.

n = int(input("Enter a number: "))

def fizz_buzz(n):
    fizzbuzz_count = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    print(f"Total FizzBuzz: {fizzbuzz_count}")
        
fizz_buzz(n)