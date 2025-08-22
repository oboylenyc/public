#Difficulty: Beginner
#
#Challenge Description:
#Write a function that takes a list of integers (which may contain duplicates and may not be sorted) and returns a new list containing only the unique numbers, sorted in ascending order.

import random

numbers=[10, -1, 10, 0, -1, 2]
#numbers = list(range(10))
#random.shuffle(numbers)

def unique_sorted(numbers):
    # Step 1: remove duplicates manually
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)

    # Step 2: bubble sort
    n = len(unique)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]
                swapped = True
        if not swapped:
            break

    return unique


# Example test
print(numbers)
print(unique_sorted(numbers))