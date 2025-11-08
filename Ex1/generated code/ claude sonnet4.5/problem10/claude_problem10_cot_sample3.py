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
    # Define all even single digits
    even_digits = [0, 2, 4, 6, 8]
    
    # Normalize range
    lower = min(a, b)
    upper = max(a, b)
    
    # Filter even digits that fall within the range
    result = [digit for digit in even_digits if lower <= digit <= upper]
    
    return result

