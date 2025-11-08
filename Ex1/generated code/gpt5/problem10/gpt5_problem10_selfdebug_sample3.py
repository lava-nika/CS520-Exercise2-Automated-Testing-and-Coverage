from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Arithmetic stepping: compute first even >= lo, step by 2 up to min(hi, 8).
    """
    lo, hi = (a, b) if a <= b else (b, a)
    top = min(hi, 8)
    if top < 2:
        return []
    # first even >= lo
    start = lo if lo % 2 == 0 else lo + 1
    start = max(start, 2)
    if start > top:
        return []
    return list(range(start, top + 1, 2))