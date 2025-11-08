from typing import List, Optional
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Bucketization / hashing approach (expected O(n)).

    Buckets have width = threshold. Any pair with difference < threshold must fall
    into the same bucket or adjacent buckets.

    >>> has_close_elements_bucket([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements_bucket([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if threshold <= 0 or len(numbers) < 2:
        return False

    buckets: dict[int, float] = {}

    for x in numbers:
        # Skip NaNs
        if isinstance(x, float) and math.isnan(x):
            continue

        b = math.floor(x / threshold)

        # Same bucket → guaranteed < threshold
        if b in buckets:
            return True

        # Neighboring buckets might still be < threshold
        left = b - 1
        right = b + 1

        if left in buckets and abs(x - buckets[left]) < threshold:
            return True
        if right in buckets and abs(x - buckets[right]) < threshold:
            return True

        buckets[b] = x

    return False