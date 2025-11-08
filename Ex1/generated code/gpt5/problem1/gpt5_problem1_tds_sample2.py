from typing import List, Optional
import math
from collections import defaultdict

def _filter_numbers(numbers: Optional[List[float]]) -> List[float]:
    """Return a cleaned list with only finite floats, ignoring None/NaN."""
    if not numbers:
        return []
    out: List[float] = []
    for x in numbers:
        if x is None:
            continue
        # Accept ints as floats as well
        try:
            xf = float(x)
        except (TypeError, ValueError):
            continue
        if math.isfinite(xf):
            out.append(xf)
    return out

# Approach 2: Brute-force pairwise comparison with early exit (O(n^2))
def has_close_elements(numbers: List[float] | None, threshold: float) -> bool:
    if threshold is None or threshold <= 0:
        return False
    arr = _filter_numbers(numbers)
    n = len(arr)
    if n < 2:
        return False
    for i in range(n):
        ai = arr[i]
        # Early exit if two equal values and threshold > 0 (difference 0 < threshold)
        for j in range(i + 1, n):
            if abs(ai - arr[j]) < threshold:
                return True
    return False