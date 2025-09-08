""" Title
Recursive Fibonacci Sequence

Difficulty: Intermediate

Challenge Description:
Write a recursive function fibonacci(n) that returns the n-th number in the Fibonacci sequence.

The sequence starts with 0, 1, and each subsequent number is the sum of the two before it.

Assume n will always be a non-negative integer.

Use recursion only (no loops, no memoization). """

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage: find the 6th Fibonacci number
print(fibonacci(6))  # Expected output: 8


# Bonus: print the first n Fibonacci numbers
def print_fibonacci_sequence(n: int) -> None:
    """Print the first n Fibonacci numbers using recursion."""
    sequence = [fibonacci(i) for i in range(n)]
    print(" ".join(map(str, sequence)))


# Example usage: print first 7 Fibonacci numbers
print_fibonacci_sequence(7)  # Expected output: 0 1 1 2 3 5 8