""" Title: Recursive Digit Sum

Difficulty: Intermediate

Challenge Description:
Write a recursive function digit_sum(n) that takes a positive integer n and returns the sum of its digits. You must solve it using recursion (no loops).

Constraints:

Assume n is always a positive integer.

Use recursion only, not iteration. """

def digit_sum(n: int) -> int:
    # Base case: single digit
    if n < 10:
        return n
    # Recursive case: last digit + sum of remaining digits
    return n % 10 + digit_sum(n // 10)

def digital_root(n: int) -> int:
    if n < 10:
        return n
    return digital_root(digit_sum(n))

# Example usage
print(digital_root(472))   # 4 (since 4+7+2=13 → 1+3=4)
print(digital_root(9999))  # 9 (since 9+9+9+9=36 → 3+6=9)