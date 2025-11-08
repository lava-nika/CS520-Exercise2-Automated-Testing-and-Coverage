from typing import List

# Mapping index by digit; index 0 unused
_DIGIT_TO_NAME = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

def by_length(arr: List[int]) -> List[str]:
    """
    Keep only 1..9, sort descending, map to English names.
    """
    # Filter to valid digits only
    digits = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    if not digits:
        return []
    # Sort descending in one pass (avoids sort ascending then reverse)
    digits.sort(reverse=True)
    # Map digits to their names
    return [_DIGIT_TO_NAME[d] for d in digits]
