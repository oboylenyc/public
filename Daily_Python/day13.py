""" Title: Sorting Student Scores

Difficulty: Intermediate

Challenge Description:
Write a function that takes in a list of student records, where each record is a tuple (name, score). Your task is to return a new list of these records sorted by score in descending order. If two students have the same score, sort them alphabetically by name (ascending).

Constraints:

You must not use sorted() with a lambda key directly. Instead, practice writing your own comparison or implement a simple sorting algorithm (like bubble sort, insertion sort, or selection sort). """

def sort_students(students, method="builtin"):
    if method == "builtin":
        # Score descending, then name ascending
        return sorted(students, key=lambda x: (-x[1], x[0]))
    
    elif method == "manual":
        arr = students[:]  # don't mutate input
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and (
                arr[j][1] < key[1] or
                (arr[j][1] == key[1] and arr[j][0] > key[0])
            ):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    else:
        raise ValueError("method must be 'builtin' or 'manual'")


# Demo
students = [("Alice", 88), ("Bob", 95), ("Charlie", 88), ("David", 72)]

print("Builtin:", sort_students(students, "builtin"))
print("Manual:", sort_students(students, "manual"))
