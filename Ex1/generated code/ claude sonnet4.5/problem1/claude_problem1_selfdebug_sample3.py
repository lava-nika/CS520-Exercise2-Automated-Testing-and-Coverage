from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    sorted_numbers = sorted(numbers)
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True
    return False

