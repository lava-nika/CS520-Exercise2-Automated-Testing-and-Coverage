from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Edge case: need at least 2 numbers to compare
    if len(numbers) < 2:
        return False
    
    # Sort the list - closest numbers will be adjacent
    sorted_numbers = sorted(numbers)
    
    # Check only adjacent pairs
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True
    
    return False

