from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers are closer than the given threshold.

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
    >>> has_close_elements([1.0, float('inf')], 1e9)
    False
    """
    n = len(numbers)
    if n < 2:
        return False

    # Sorting enables checking only adjacent differences
    nums = sorted(numbers)

    # Check adjacent pairs
    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        # diff is non-negative because the list is sorted
        # We need strictly less than threshold
        if diff < threshold:
            return True

    return False


if __name__ == "__main__":
    # Simple sanity checks
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True
    assert has_close_elements([], 1.0) is False
    assert has_close_elements([2.0], 1.0) is False
    assert has_close_elements([2.0, 2.0], 0.0) is False
    assert has_close_elements([2.0, 2.0], 0.1) is True
    print("All tests passed.")
