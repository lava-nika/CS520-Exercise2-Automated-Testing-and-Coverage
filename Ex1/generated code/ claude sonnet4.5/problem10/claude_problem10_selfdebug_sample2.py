def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    lower = min(a, b)
    upper = max(a, b)
    
    lower = max(0, lower)
    upper = min(9, upper)
    
    result = []
    for num in range(lower, upper + 1):
        if num % 2 == 0:
            result.append(num)
    
    return result

