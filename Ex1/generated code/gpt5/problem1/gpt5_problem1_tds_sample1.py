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

# Approach 1: Sort then check adjacent differences (O(n log n))
def has_close_elements(numbers: List[float] | None, threshold: float) -> bool:
    # Threshold <= 0 means no positive distance can be < threshold
    if threshold is None or threshold <= 0:
        return False
    arr = _filter_numbers(numbers)
    if len(arr) < 2:
        return False
    arr.sort()
    # Check neighbors; this is sufficient because sorted order minimizes distance among neighbors
    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) < threshold:
            return True
    return False