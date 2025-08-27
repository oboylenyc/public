""" Title: Recursive Factorial

Difficulty: Intermediate

Challenge Description:
Write a recursive function factorial(n) that returns the factorial of a given positive integer n.

The factorial of n is defined as:

n! = n * (n-1) * (n-2) * ... * 1

By definition, 0! = 1.

You must use recursion (no loops).

Assume input will always be a non-negative integer. """

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # 120
print(factorial(0))  # 1
