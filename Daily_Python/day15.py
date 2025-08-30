""" Title
Recursive Factorial Calculator

Difficulty: Intermediate

Challenge Description:
Write a recursive function factorial(n) that returns the factorial of a non-negative integer n.

The factorial of 0 is defined as 1.

For positive integers, factorial(n) = n * factorial(n-1).

Do not use loops or the math module; recursion only.

Assume input will always be a non-negative integer. """

def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}Entering factorial({n})")

    if n == 0:
        print(f"{indent}Returning 1")
        return 1

    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}Returning {result} from factorial({n})")
    return result

# Example usage
print("Final result:", factorial(4))