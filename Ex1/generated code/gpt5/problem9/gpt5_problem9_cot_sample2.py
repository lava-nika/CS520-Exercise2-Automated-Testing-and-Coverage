from typing import List

# Shared mapping (index by digit)
_DIGIT_NAMES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def by_length(arr: List[int]) -> List[str]:
    """
    Pythonic approach: filter valid digits, sort descending, map to names.
    """
    # keep only digits 1..9 (ignore everything else)
    digits = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    if not digits:
        return []
    # descending order
    digits.sort(reverse=True)
    # map to words
    return [_DIGIT_NAMES[d] for d in digits]