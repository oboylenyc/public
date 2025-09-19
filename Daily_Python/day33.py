""" Sliding Window Averages (Generators)

Difficulty: Intermediate

Challenge Description: Write a generator function sliding_averages(nums, k) that yields the average of each contiguous window of size k over the input iterable nums without loading all data into memory at once. Constraints:

nums can be any iterable of integers/floats.

k is a positive integer (k ≥ 1) and must be ≤ the number of items available; if not, raise a ValueError with a clear message.

Use O(k) extra space and O(n) time by updating a running sum as the window slides.

Yield each average as a float with full precision (don’t round).

Input Example
nums = [2, 4, 6, 8, 10]
k = 3

Expected Output
2.0, 4.0, 6.0 (i.e., the generator would yield 4.0, 6.0, 8.0? wait—correct for given example: windows are [2,4,6]→4.0, [4,6,8]→6.0, [6,8,10]→8.0)

Bonus (optional): Accept any iterable (e.g., a file stream). If nums is an iterator that can be exhausted, ensure your function doesn’t iterate it more than once. """

from collections import deque
from typing import Iterable, Generator

def sliding_averages(nums: Iterable[float], k: int) -> Generator[float, None, None]:
    """
    Yields the average of each contiguous window of size k from nums.
    
    nums: any iterable of numbers
    k: size of sliding window (must be >=1 and <= len(nums) if nums is finite)
    """
    if k < 1:
        raise ValueError("Window size k must be at least 1.")

    window = deque()
    total = 0.0
    it = iter(nums)

    # Fill the first window
    for _ in range(k):
        try:
            val = next(it)
        except StopIteration:
            raise ValueError("Window size k must be less than or equal to the number of items.")
        window.append(val)
        total += val

    yield total / k

    # Slide the window
    for val in it:
        total += val
        total -= window.popleft()
        window.append(val)
        yield total / k


# Example usage:
nums = [2, 4, 6, 8, 10]
k = 3

for avg in sliding_averages(nums, k):
    print(avg)
