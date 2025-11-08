from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Edge case: need at least 2 numbers to compare
    if len(numbers) < 2:
        return False
    
    # Compare every pair of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate absolute difference
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    
    return False

