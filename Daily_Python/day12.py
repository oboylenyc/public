""" Title: Recursive Sum of Digits

Difficulty: Intermediate

Challenge Description:
Write a recursive function sum_of_digits(n) that takes a positive integer n and returns the sum of its digits.

You must use recursion (no loops or built-in shortcuts like sum(map(int, str(n)))).

The function should stop when n becomes a single digit. """

def sum_of_digits(n: int) -> int:
    # Base case: if n is a single digit, return it
    if n < 10:
        return n
    # Recursive case: take last digit + sum of remaining digits
    return (n % 10) + sum_of_digits(n // 10)


# Bonus: digital root using recursion
def digital_root(n: int) -> int:
    if n < 10:
        return n
    return digital_root(sum_of_digits(n))


# Example runs
print(sum_of_digits(942))      # 15
print(digital_root(942))       # 6
print(digital_root(493193))    # 2