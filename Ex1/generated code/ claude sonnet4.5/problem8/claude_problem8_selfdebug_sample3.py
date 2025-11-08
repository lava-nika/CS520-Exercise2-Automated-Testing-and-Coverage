import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0 using Bisection method.
    """
    a, b = -1000.0, 1000.0
    
    while poly(xs, a) * poly(xs, b) > 0:
        a *= 2
        b *= 2
    
    tolerance = 1e-10
    max_iterations = 1000
    
    for _ in range(max_iterations):
        c = (a + b) / 2.0
        fc = poly(xs, c)
        
        if abs(fc) < tolerance or abs(b - a) < tolerance:
            return c
        
        if poly(xs, a) * fc < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2.0

