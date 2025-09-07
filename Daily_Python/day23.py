""" Recursive Sum of Digits

Difficulty: Intermediate

Challenge Description:
Write a recursive function sum_of_digits(n) that takes a positive integer n and returns the sum of its digits.

Do not use loops or string conversion to solve it — recursion only.

Base case: if n is a single digit, return n.

Recursive case: peel off the last digit and add it to the result of the recursive call on the rest of the number. """

def sum_of_digits(n: int) -> int:
    """Return the sum of digits of n using recursion."""
    if n < 10:  # base case: single digit
        return n
    return n % 10 + sum_of_digits(n // 10)


def digital_root(n: int) -> int:
    """Return the digital root of n using recursion."""
    if n < 10:  # base case: single digit
        return n
    return digital_root(sum_of_digits(n))


# Example usage
print(sum_of_digits(9875))   # 29
print(digital_root(9875))    # 2
