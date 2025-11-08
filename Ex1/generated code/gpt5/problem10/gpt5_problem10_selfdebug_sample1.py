from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b (inclusive), in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    # Strict type checks: ensure true integers, not booleans
    if not (isinstance(a, int) and not isinstance(a, bool)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) and not isinstance(b, bool)):
        raise TypeError("b must be an integer")

    lo, hi = min(a, b), max(a, b)
    even_digits = [0, 2, 4, 6, 8]
    return [d for d in even_digits if lo <= d <= hi]
