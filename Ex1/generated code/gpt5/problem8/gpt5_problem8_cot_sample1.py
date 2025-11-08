import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    """
    Evaluate polynomial with coefficients xs at point x.
    Computes: xs[0] + xs[1]*x + xs[2]*x^2 + ... + xs[n]*x^n

    Uses Horner's method for numerical stability and O(n) time.
    """
    result = 0.0
    for coeff in reversed(xs):
        result = result * x + coeff
    return result

def find_zero(xs: List[float]) -> float:
    """Find a real number x such that poly(xs, x) ~= 0.

    Requirements (as per problem statement):
      - xs must have an even number of coefficients (so the degree is odd),
      - the highest-degree (leading) coefficient must be non-zero,
      which ensures the existence of a real root.

    Strategy:
      - Expand a symmetric interval [-1, 1] until f(a) and f(b) have opposite signs.
      - Apply bisection on the bracketed interval.

    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # -6 + 11x - 6x^2 + x^3
    1.0
    """
    if not xs:
        raise ValueError("Coefficient list must not be empty.")
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients (odd-degree polynomial).")
    if xs[-1] == 0:
        raise ValueError("Leading coefficient must be non-zero.")

    f = lambda t: poly(xs, t)

    # Step 1: bracket a root
    a, b = -1.0, 1.0
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b

    # Expand interval until sign change is observed
    # (Odd degree ensures this will happen for large |x|.)
    max_expand = 100
    for _ in range(max_expand):
        if fa * fb < 0:
            break
        a *= 2.0
        b *= 2.0
        fa, fb = f(a), f(b)
        if fa == 0.0:
            return a
        if fb == 0.0:
            return b
    else:
        # Shouldn't happen for valid odd-degree polynomials with non-zero leading coefficient,
        # but guard anyway.
        raise RuntimeError("Failed to bracket a root. Check coefficients.")

    # Step 2: bisection
    tol = 1e-12
    max_iter = 200
    for _ in range(max_iter):
        mid = 0.5 * (a + b)
        fm = f(mid)

        # Convergence checks: function value or interval size
        if abs(fm) <= tol:
            return mid
        if abs(b - a) <= tol * max(1.0, abs(a), abs(b)):
            return mid

        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm

    # Return midpoint if max iterations hit (close enough)
    return 0.5 * (a + b)
