""" Difficulty: Intermediate

Challenge Description:
Write a function safe_divide(a, b) that attempts to divide a by b.

If the division works, return the result.

If b is zero, return the string "Error: Division by zero".

If either a or b is not a number (int or float), return the string "Error: Invalid input". """

def safe_divide(a, b):
    try:
        # Check if inputs are numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Error: Invalid input"

        # Try division
        result = a / b

        # Bonus: return int if result is whole number
        if result.is_integer():
            return int(result)
        return result

    except ZeroDivisionError:
        return "Error: Division by zero"

print(safe_divide(10, 2))    # 5
print(safe_divide(5, 0))     # Error: Division by zero
print(safe_divide("apple", 3))  # Error: Invalid input
print(safe_divide(7, 2))     # 3.5