from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Solution B: arithmetic stepping with clamping to the digit range.
    Computes the first even >= lo, then steps by 2 up to min(hi, 8).
    """
    lo, hi = (a, b) if a <= b else (b, a)
    # There are no even single-digit numbers below 2, or above 8.
    top = min(hi, 8)
    if top < 2:
        return []
    start = lo if lo % 2 == 0 else lo + 1
    start = max(start, 2)
    if start > top:
        return []
    return list(range(start, top + 1, 2))