""" Title: Recursive Binary Search

Difficulty: Intermediate

Challenge Description:
Write a function binary_search(arr, target) that uses recursion to determine whether target exists in a sorted list arr.

If the target is found, return its index.

If it’s not found, return -1.

Assume the list contains unique integers sorted in ascending order.

Constraints:

Do not use built-in search functions (in, .index() etc.).

Implement it recursively, not iteratively. """

def binary_search(arr, target, left=0, right=None, depth=0):
    if right is None:
        right = len(arr) - 1

    # Base case: not found
    if left > right:
        return -1, depth

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid, depth + 1  # Found target
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1, depth + 1)
    else:
        return binary_search(arr, target, mid + 1, right, depth + 1)


# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7

index, calls = binary_search(arr, target)
print("Index:", index)
print("Recursive calls:", calls)

target = 4
index, calls = binary_search(arr, target)
print("Index:", index)
print("Recursive calls:", calls)