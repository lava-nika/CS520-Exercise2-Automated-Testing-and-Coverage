import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    # Smart initial range based on coefficient magnitudes
    max_coeff = max(abs(c) for c in xs if c != 0)
    initial_range = max(10, max_coeff * 10)
    
    left, right = -initial_range, initial_range
    
    # Expand range if necessary
    max_expansions = 10
    for _ in range(max_expansions):
        if poly(xs, left) * poly(xs, right) <= 0:
            break
        left *= 2
        right *= 2
    
    # Bisection
    tolerance = 1e-6
    while right - left > tolerance:
        mid = (left + right) / 2.0
        f_mid = poly(xs, mid)
        
        if abs(f_mid) < tolerance:
            return mid
        
        f_left = poly(xs, left)
        
        if f_left * f_mid < 0:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2.0

