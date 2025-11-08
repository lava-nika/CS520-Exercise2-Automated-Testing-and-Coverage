import math
from typing import List, Iterable

def _strip_trailing_zeros(xs: Iterable[float]) -> List[float]:
    xs = list(xs)
    # Remove trailing zeros to reflect true degree
    i = len(xs) - 1
    while i >= 0 and xs[i] == 0:
        i -= 1
    return xs[:i+1]

def poly(xs: List[float], x: float) -> float:
    """
    Evaluate polynomial with coefficients xs at point x.
    Computes: xs[0] + xs[1]*x + xs[2]*x^2 + ... + xs[n]*x^n

    Uses Horner's method (stable and O(n)).
    """
    # Horner's method
    result = 0.0
    for coeff in reversed(xs):
        result = result * x + coeff
    return result

def find_zero(xs: List[float]) -> float:
    """Find a real x such that poly(xs, x) ~= 0.

    Requirements (per problem):
    - xs must have an even number of coefficients (so degree is odd),
    - the largest-degree (leading) coefficient must be non-zero.
    Under these conditions, a real root exists.

    Strategy:
    - Exponentially expand a symmetric interval until f(a) and f(b) have
      opposite signs (root bracketing).
    - Apply bisection to converge to a root.

    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # -6 + 11x - 6x^2 + x^3
    1.0
    """
    xs = _strip_trailing_zeros(xs)
    if not xs:
        raise ValueError("Coefficient list must not be empty or all zeros.")
    if len(xs) % 2 != 0:
        # After stripping trailing zeros, even number of coefficients ⇒ odd degree
        # If it's odd, then degree is even: out of spec guarantees.
        raise ValueError("xs must have an even number of coefficients (odd-degree polynomial).")
    if xs[-1] == 0:
        raise ValueError("Leading (largest-degree) coefficient must be non-zero.")

    def f(t: float) -> float:
        return poly(xs, t)

    # 1) Bracket a root
    a, b = -1.0, 1.0
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b

    max_expand = 100
    for _ in range(max_expand):
        if fa * fb < 0:
            break
        # Expand symmetrically
        a *= 2.0
        b *= 2.0
        fa, fb = f(a), f(b)
        if fa == 0.0:
            return a
        if fb == 0.0:
            return b
    else:
        # Should not happen for odd-degree polynomials with nonzero leading coeff
        raise RuntimeError("Failed to bracket a root. Check coefficients.")

    # 2) Bisection
    tol = 1e-12
    max_iter = 200
    for _ in range(max_iter):
        mid = 0.5 * (a + b)
        fm = f(mid)

        # Convergence checks
        if abs(fm) <= tol:
            return mid
        if abs(b - a) <= tol * max(1.0, abs(a), abs(b)):
            return mid

        # Keep the subinterval with a sign change
        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm

    # If iterations exhausted, return best midpoint
    return 0.5 * (a + b)
