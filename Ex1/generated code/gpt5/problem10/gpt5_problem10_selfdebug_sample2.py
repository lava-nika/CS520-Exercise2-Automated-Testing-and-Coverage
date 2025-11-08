from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Fixed-set filter over even digits {2,4,6,8}.
    """
    lo, hi = (a, b) if a <= b else (b, a)
    candidates = [2, 4, 6, 8]
    return [d for d in candidates if lo <= d <= hi]