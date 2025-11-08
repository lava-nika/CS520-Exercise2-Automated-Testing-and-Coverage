from typing import List, Optional

_ALLOWED_EVEN_DIGITS = (2, 4, 6, 8)

def _normalize_bounds(a: Optional[int], b: Optional[int]) -> Optional[tuple[int, int]]:
    """Return (lo, hi) as integers if both valid; otherwise None.
       We only care about even *digits*, which are in {2,4,6,8} ⊆ [1,9].
       If either bound is None or non-integer-castable, we return None."""
    if not isinstance(a, int) or not isinstance(b, int):
        return None
    lo, hi = (a, b) if a <= b else (b, a)
    return lo, hi

# Implementation 1: Filter a fixed universe of even digits
def generate_integers(a, b) -> List[int]:
    bounds = _normalize_bounds(a, b)
    if bounds is None:
        return []
    lo, hi = bounds
    return [d for d in _ALLOWED_EVEN_DIGITS if lo <= d <= hi]