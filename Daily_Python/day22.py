""" Implement Bubble Sort

Difficulty: Intermediate

Challenge Description:
Write a function bubble_sort(numbers: list[int]) -> list[int] that sorts a list of integers in ascending order using the bubble sort algorithm.

Do not use Python’s built-in sorted() or .sort().

The function should return a new sorted list (not modify in place).

Bubble sort works by repeatedly stepping through the list, comparing adjacent pairs, and swapping them if they are in the wrong order. Continue until no swaps are needed.

Input Example
[5, 2, 9, 1, 5, 6]

Expected Output
[1, 2, 5, 5, 6, 9] """

def bubble_sort(numbers: list[int], descending: bool = False) -> list[int]:
    arr = numbers[:]  # make a copy so the original list is not modified
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (not descending and arr[j] > arr[j + 1]) or (descending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:  # if no swaps in this pass, list is sorted
            break

    return arr


# Example usage:
print(bubble_sort([5, 2, 9, 1, 5, 6]))           # [1, 2, 5, 5, 6, 9]
print(bubble_sort([5, 2, 9, 1, 5, 6], True))     # [9, 6, 5, 5, 2, 1]