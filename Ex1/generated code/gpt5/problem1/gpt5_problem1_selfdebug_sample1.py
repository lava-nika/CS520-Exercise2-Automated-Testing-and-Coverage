from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers are closer than the given (strict) threshold.
    
    Returns True if there exist i != j such that |numbers[i] - numbers[j]| < threshold.
    The check is strict: equality to threshold does not count.

    Approach: sort and compare adjacent elements.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    >>> has_close_elements([], 1.0)
    False
    >>> has_close_elements([2.0], 1.0)
    False
    >>> has_close_elements([2.0, 2.0], 0.0)
    False
    >>> has_close_elements([2.0, 2.0], 0.1)
    True
    """
    n = len(numbers)
    if n < 2:
        return False

    # If threshold <= 0, no non-negative difference can be strictly less than it.
    if threshold <= 0:
        return False

    nums = sorted(numbers)
    for i in range(1, n):
        # In sorted order, nums[i] - nums[i-1] is the minimal absolute diff involving nums[i]
        if nums[i] - nums[i - 1] < threshold:
            return True
    return False
