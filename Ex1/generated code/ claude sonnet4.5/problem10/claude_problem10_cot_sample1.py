def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    
    Note: Only single-digit numbers (0-9) are considered.
    """
    # Step 1: Normalize the range (handle a > b or b > a)
    lower = min(a, b)
    upper = max(a, b)
    
    # Step 2: Constrain to single-digit range [0, 9]
    lower = max(lower, 0)  # Can't go below 0 for digits
    upper = min(upper, 9)  # Can't go above 9 for single digits
    
    # Step 3: Collect even digits in the range
    result = []
    for digit in range(lower, upper + 1):
        if digit % 2 == 0:  # Check if even
            result.append(digit)
    
    return result