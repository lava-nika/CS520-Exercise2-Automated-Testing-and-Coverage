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

# Approach 3: Bucketization (linear expected time)
# Idea: Use buckets of width = threshold. If two numbers fall into the same bucket
# or neighboring buckets, they *might* be closer than threshold; verify precisely.
def has_close_elements(numbers: List[float] | None, threshold: float) -> bool:
    if threshold is None or threshold <= 0:
        return False
    arr = _filter_numbers(numbers)
    if len(arr) < 2:
        return False

    bucket_size = threshold  # strictly positive
    buckets: dict[int, list[float]] = defaultdict(list)

    for x in arr:
        idx = math.floor(x / bucket_size)
        # Check current and neighbor buckets
        for k in (idx - 1, idx, idx + 1):
            for y in buckets.get(k, []):
                if abs(x - y) < threshold:
                    return True
        buckets[idx].append(x)

    return False