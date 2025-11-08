from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Solution A: filter from a fixed set of even digits {2,4,6,8}
    that lie within [min(a,b), max(a,b)].
    """
    lo, hi = (a, b) if a <= b else (b, a)
    even_digits = [2, 4, 6, 8]
    return [d for d in even_digits if lo <= d <= hi]
