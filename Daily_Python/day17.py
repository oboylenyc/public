""" Read and Write Numbers

Difficulty: Intermediate

Challenge Description:
Write a program that:

Reads integers from a text file called numbers.txt (one number per line).

Calculates the sum of all numbers.

Writes the result to a new file called sum.txt.

Constraints:

Assume the input file may contain extra spaces or blank lines, which should be ignored.

Handle both positive and negative integers. """

def process_numbers(input_file="numbers.txt", output_file="sum.txt"):
    numbers = []
    
    # Read numbers from file
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip blank lines
                numbers.append(int(line))
    
    # Calculate results
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    
    # Write results to file
    with open(output_file, "w") as f:
        f.write(f"{total}\n")
        f.write(f"{avg:.2f}\n")


# Run the function (assuming numbers.txt exists in the same folder)
process_numbers()
def process_numbers(input_file="numbers.txt", output_file="sum.txt"):
    numbers = []
    
    # Read numbers from file
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip blank lines
                numbers.append(int(line))
    
    # Calculate results
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    
    # Write results to file
    with open(output_file, "w") as f:
        f.write(f"{total}\n")
        f.write(f"{avg:.2f}\n")


# Run the function (assuming numbers.txt exists in the same folder)
process_numbers()