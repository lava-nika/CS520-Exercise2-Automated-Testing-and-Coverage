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
    Derivative of xs[0] + xs[1]*x + xs[2]*x^2 + ... is:
    xs[1] + 2*xs[2]*x + 3*xs[3]*x^2 + ...
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    
    Uses Newton-Raphson method: x_{n+1} = x_n - f(x_n) / f'(x_n)
    
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3)
    1.0
    """
    # Initial guess (using 0 as starting point)
    x = 0.0
    
    # Newton-Raphson iteration
    max_iterations = 1000
    tolerance = 1e-10
    
    for _ in range(max_iterations):
        # Calculate f(x) and f'(x)
        fx = poly(xs, x)
        fpx = poly_derivative(xs, x)
        
        # Check for convergence
        if abs(fx) < tolerance:
            return x
        
        # Avoid division by zero
        if abs(fpx) < 1e-15:
            # Derivative is too small, perturb x
            x += 0.1
            continue
        
        # Newton-Raphson update
        x_new = x - fx / fpx
        
        # Check if change is small enough (convergence)
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    return x

