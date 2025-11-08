import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    
    Uses Bisection method to find root.
    
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3)
    1.0
    """
    # First, find an interval [a, b] where f(a) and f(b) have opposite signs
    # Since we have odd-degree polynomial (even number of coefficients),
    # it must cross the x-axis
    
    # Search for initial bracket
    a, b = -1000.0, 1000.0
    
    # Expand search range if needed
    while poly(xs, a) * poly(xs, b) > 0:
        a *= 2
        b *= 2
    
    # Bisection method
    tolerance = 1e-10
    max_iterations = 1000
    
    for _ in range(max_iterations):
        # Find midpoint
        c = (a + b) / 2.0
        fc = poly(xs, c)
        
        # Check for convergence
        if abs(fc) < tolerance or abs(b - a) < tolerance:
            return c
        
        # Determine which half contains the root
        if poly(xs, a) * fc < 0:
            # Root is in [a, c]
            b = c
        else:
            # Root is in [c, b]
            a = c
    
    return (a + b) / 2.0

