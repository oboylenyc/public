""" Comprehensions: Student Grade Summary

Difficulty: Intermediate

Challenge Description: Implement a function summarize(grades) that takes a list of (name, score) tuples and returns a dictionary mapping each student’s normalized name (title case) to "Pass" or "Fail". Rules:

Passing is score ≥ 60.

Ignore any records with scores outside 0–100.

If a student appears multiple times, keep the highest valid score.

You must use at least one list comprehension and one dict (or set) comprehension somewhere in your solution.

Do not use external libraries.

Input Example
[("alice", 58), ("Bob", 92), ("ALICE", 61), ("Eve", -3), ("bob", 87), ("ChArLiE", 60), ("Dana", 101)]

Expected Output
{"Alice": "Pass", "Bob": "Pass", "Charlie": "Pass"}

Bonus (optional): Also return a sorted list of just the passing students’ names (alphabetical) alongside the dictionary, e.g., (summary_dict, ["Alice", "Bob", "Charlie"]). """

def summarize(grades):
    # Filter out invalid scores
    valid_grades = [(name.title(), score) for name, score in grades if 0 <= score <= 100]

    # Keep the highest score for each student
    best_scores = {}
    for name, score in valid_grades:
        best_scores[name] = max(score, best_scores.get(name, 0))

    # Build summary dictionary
    summary = {name: ("Pass" if score >= 60 else "Fail") for name, score in best_scores.items()}

    # Bonus: sorted list of passing students
    passing = sorted([name for name, result in summary.items() if result == "Pass"])

    return summary, passing


# Example usage
grades = [
    ("alice", 58),
    ("Bob", 92),
    ("ALICE", 61),
    ("Eve", -3),
    ("bob", 87),
    ("ChArLiE", 60),
    ("Dana", 101),
]

print(summarize(grades))
