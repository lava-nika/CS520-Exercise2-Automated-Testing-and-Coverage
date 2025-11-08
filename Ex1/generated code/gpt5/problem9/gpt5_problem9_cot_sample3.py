from typing import List

# Shared mapping (index by digit)
_DIGIT_NAMES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def by_length(arr: List[int]) -> List[str]:
    """
    Counting approach: count occurrences of each digit 1..9, then build
    the result from 9 down to 1.
    """
    counts = [0] * 10  # index 0..9
    for x in arr:
        if isinstance(x, int) and 1 <= x <= 9:
            counts[x] += 1

    result: List[str] = []
    for d in range(9, 1 - 1, -1):  # 9 down to 1
        if counts[d]:
            result.extend([_DIGIT_NAMES[d]] * counts[d])
    return result