import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    left, right = -1000, 1000
    
    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2
    
    tolerance = 1e-6
    while right - left > tolerance:
        mid = (left + right) / 2
        mid_value = poly(xs, mid)
        
        if abs(mid_value) < tolerance:
            return mid
        
        if poly(xs, left) * mid_value < 0:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2

