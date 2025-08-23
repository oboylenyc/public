#Title: Word Counter
#
#Difficulty: Intermediate
#
#Challenge Description:
#Write a program that reads the contents of a text file named sample.txt and counts how many times each word appears. Treat words as case-insensitive (so "Python" and "python" are the same word). Ignore punctuation like commas and periods.
#
#Your program should print each word alongside its frequency, sorted by frequency in descending order.
#
#Input Example (contents of sample.txt):
import string

counts = {}

try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
    content = ""  # so later code doesn't break
except Exception as e:
    print(f"An error occurred: {e}")
    content = ""

# Normalize text: lowercase + remove punctuation
content = content.lower()
for punct in string.punctuation:
    content = content.replace(punct, "")

# Split into words
words = content.split()

# Count word frequencies
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Sort results
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Write to a new file
with open("word_count.txt", "w") as out_file:
    for word, freq in sorted_counts:
        out_file.write(f"{word}: {freq}\n")

print("Word counts have been written to 'word_count.txt'")