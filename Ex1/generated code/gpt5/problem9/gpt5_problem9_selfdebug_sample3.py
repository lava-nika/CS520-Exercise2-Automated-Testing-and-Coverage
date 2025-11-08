from typing import List

# Mapping index by digit; index 0 unused
_DIGIT_TO_NAME = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def by_length(arr: List[int]) -> List[str]:
    """
    Use counting sort specialized for digits 1..9 to avoid O(n log n) sort.
    """
    counts = [0] * 10  # 0..9 (0 unused for output)
    for x in arr:
        if isinstance(x, int) and 1 <= x <= 9:
            counts[x] += 1

    result: List[str] = []
    # Build descending: 9, 8, ..., 1
    for d in range(9, 0, -1):
        c = counts[d]
        if c:
            result.extend([_DIGIT_TO_NAME[d]] * c)
    return result
