from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Sort + adjacent scan approach (O(n log n)).

    >>> has_close_elements_sorting([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements_sorting([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if threshold <= 0 or len(numbers) < 2:
        return False

    # Remove NaNs; they break comparisons
    nums = [x for x in numbers if not (isinstance(x, float) and math.isnan(x))]
    if len(nums) < 2:
        return False

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] < threshold:
            return True
    return False