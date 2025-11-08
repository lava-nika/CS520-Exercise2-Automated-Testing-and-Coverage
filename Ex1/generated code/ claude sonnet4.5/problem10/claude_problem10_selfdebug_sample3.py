def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    even_digits = [0, 2, 4, 6, 8]
    lower = min(a, b)
    upper = max(a, b)
    
    return [digit for digit in even_digits if lower <= digit <= upper]

