import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_derivative(xs: list, x: float):
    """
    Evaluates the derivative of polynomial with coefficients xs at point x.
    If f(x) = xs[0] + xs[1]*x + xs[2]*x^2 + ... + xs[n]*x^n
    Then f'(x) = xs[1] + 2*xs[2]*x + 3*xs[3]*x^2 + ... + n*xs[n]*x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

def find_zero(xs: list):
    """
    Improved version with better handling of edge cases.
    Uses Newton-Raphson with multiple initial guesses if needed.
    """
    def try_newton_raphson(x_start, xs, max_iter=1000, tol=1e-10):
        """Try Newton-Raphson from a given starting point"""
        x = x_start
        
        for _ in range(max_iter):
            fx = poly(xs, x)
            fpx = poly_derivative(xs, x)
            
            if abs(fx) < tol:
                return x, True
            
            if abs(fpx) < tol:
                return None, False  # Derivative too small, try different start
            
            x_new = x - fx / fpx
            
            if abs(x_new - x) < tol:
                return x_new, True
            
            # Check for divergence
            if abs(x_new) > 1e6:
                return None, False  # Diverging, try different start
            
            x = x_new
        
        return x, True  # Return best approximation found
    
    # Try multiple starting points to increase robustness
    starting_points = [0.0, 1.0, -1.0, 10.0, -10.0]
    
    for x_start in starting_points:
        result, success = try_newton_raphson(x_start, xs)
        if success and result is not None:
            # Verify it's actually a root
            if abs(poly(xs, result)) < 1e-6:
                return result
    
    # Fallback: return result from x=0 even if not perfect
    result, _ = try_newton_raphson(0.0, xs, max_iter=2000)
    return result if result is not None else 0.0