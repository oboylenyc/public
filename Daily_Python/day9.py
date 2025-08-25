#Title: Word Counter from File
#
#Difficulty: Intermediate
#
#Challenge Description:
#Write a Python program that reads a text file named input.txt and counts how many times each word appears.
#
#Ignore case (treat "The" and "the" the same).
#
#Remove punctuation (e.g., "hello," should count as "hello").
#
#Print each unique word with its count, sorted alphabetically.

import string

counts = {}

try:
    with open("input.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")
    content = ""  # so later code doesn't break
except Exception as e:
    print(f"An error occurred: {e}")
    content = ""

# Normalize text: lowercase + remove punctuation
translator = str.maketrans("", "", string.punctuation)
content = content.lower().translate(translator)

# Split into words
words = content.split()

# Count word frequencies
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Sort results alphabetically
sorted_counts = sorted(counts.items())

# Write to a new file
with open("word_count.txt", "w") as out_file:
    for word, freq in sorted_counts:
        out_file.write(f"{word}: {freq}\n")

    # Bonus: most common word(s)
    if counts:
        max_freq = max(counts.values())
        most_common = [word for word, freq in counts.items() if freq == max_freq]

        out_file.write("\nMost common word(s):\n")
        for word in most_common:
            out_file.write(f"{word}: {max_freq}\n")

print("Word counts (and most common word(s)) have been written to 'word_count.txt'")