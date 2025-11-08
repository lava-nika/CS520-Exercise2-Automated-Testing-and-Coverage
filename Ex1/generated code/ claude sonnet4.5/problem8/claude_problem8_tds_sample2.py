import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    def poly_derivative(xs, x):
        return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs) if i > 0])
    
    # Start with initial guess
    x = 0.0
    tolerance = 1e-6
    max_iterations = 1000
    
    for _ in range(max_iterations):
        fx = poly(xs, x)
        if abs(fx) < tolerance:
            return x
        
        fpx = poly_derivative(xs, x)
        if abs(fpx) < 1e-10:
            # Derivative too small, switch to bisection
            break
        
        x = x - fx / fpx
    
    # Fallback to bisection if Newton-Raphson fails
    left, right = -1000, 1000
    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2
    
    while right - left > tolerance:
        mid = (left + right) / 2
        if abs(poly(xs, mid)) < tolerance:
            return mid
        if poly(xs, left) * poly(xs, mid) < 0:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2

