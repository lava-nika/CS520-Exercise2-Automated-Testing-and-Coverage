def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        List of even single-digit numbers in range [min(a,b), max(a,b)]
    
    Examples:
        >>> generate_integers(2, 8)
        [2, 4, 6, 8]
        >>> generate_integers(8, 2)
        [2, 4, 6, 8]
        >>> generate_integers(10, 14)
        []
    """
    # Normalize the range (handle both a < b and a > b)
    lower = min(a, b)
    upper = max(a, b)
    
    # Constrain to single-digit range [0, 9]
    lower = max(0, lower)
    upper = min(9, upper)
    
    # Collect even numbers in the constrained range
    result = []
    for num in range(lower, upper + 1):
        if num % 2 == 0:
            result.append(num)
    
    return result

