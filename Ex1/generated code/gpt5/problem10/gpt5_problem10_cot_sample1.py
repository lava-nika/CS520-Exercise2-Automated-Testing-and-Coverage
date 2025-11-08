from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b (inclusive), in ascending order.

    Examples:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    lo, hi = min(a, b), max(a, b)
    even_digits = [0, 2, 4, 6, 8]
    return [d for d in even_digits if lo <= d <= hi]
