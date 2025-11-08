def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    
    FIXES:
    - Added type validation for inputs
    - Added explicit handling for non-integer types
    """
    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"Both inputs must be integers, got {type(a).__name__} and {type(b).__name__}")
    
    # Booleans are technically integers in Python, exclude them
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Boolean inputs are not allowed")
    
    # Normalize range
    lower = min(a, b)
    upper = max(a, b)
    
    # Constrain to single digits (0-9)
    lower = max(lower, 0)
    upper = min(upper, 9)
    
    # Collect even digits
    result = []
    for digit in range(lower, upper + 1):
        if digit % 2 == 0:
            result.append(digit)
    
    return result