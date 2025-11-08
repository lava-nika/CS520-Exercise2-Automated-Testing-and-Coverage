import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_derivative(xs: list, x: float):
    """
    Evaluates the derivative of polynomial at point x.
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0 using Newton-Raphson method.
    """
    x = 0.0
    max_iterations = 1000
    tolerance = 1e-10
    
    for _ in range(max_iterations):
        fx = poly(xs, x)
        fpx = poly_derivative(xs, x)
        
        if abs(fx) < tolerance:
            return x
        
        if abs(fpx) < 1e-15:
            x += 0.1
            continue
        
        x_new = x - fx / fpx
        
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    return x

