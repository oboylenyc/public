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

try:
    with open("sample.txt", "r") as file:
        content = file.read() 
        print(content)
        file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")