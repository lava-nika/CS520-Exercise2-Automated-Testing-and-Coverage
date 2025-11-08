import math
from typing import List, Tuple

# ------------------------------- Utilities -------------------------------

def _trim_trailing_zeros(xs: List[float]) -> List[float]:
    """Remove trailing zeros so the highest-degree coefficient is non-zero, if possible."""
    if not xs:
        return xs
    i = len(xs) - 1
    while i >= 0 and xs[i] == 0:
        i -= 1
    return xs[:i+1]

def _validate_coeffs(xs: List[float]) -> List[float]:
    xs = _trim_trailing_zeros(xs)
    if not xs:
        raise ValueError("Polynomial must not be identically zero or empty.")
    if len(xs) % 2 != 0:  # even number of coefficients required by prompt
        raise ValueError("xs must contain an even number of coefficients (odd-degree polynomial).")
    # Highest-degree coefficient must be non-zero now by trimming
    return xs

# --------------------------- Solution A: Bisection ---------------------------

def poly(xs: List[float], x: float) -> float:
    """Evaluate polynomial using math.pow (straightforward power-sum)."""
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def _bracket_root(xs: List[float]) -> Tuple[float, float, float, float]:
    """
    Find a bracket [a, b] with f(a)*f(b) <= 0 by expanding exponentially.
    Returns (a, b, f(a), f(b)).
    """
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)
    if fa == 0.0:
        return a, a, fa, fa
    if fb == 0.0:
        return b, b, fb, fb
    # expand until sign change or cap reached
    max_expand = 100
    k = 0
    while fa * fb > 0 and k < max_expand:
        # expand outwards
        a *= 2.0
        b *= 2.0
        fa = poly(xs, a)
        fb = poly(xs, b)
        k += 1
    return a, b, fa, fb

def find_zero(xs: List[float], tol: float = 1e-12, max_iter: int = 200) -> float:
    """
    Find one real root using bracketing + bisection (robust).
    """
    xs = _validate_coeffs(xs)

    f0 = poly(xs, 0.0)
    if abs(f0) <= tol:
        return 0.0

    a, b, fa, fb = _bracket_root(xs)
    # If we found an exact root while bracketing
    if a == b:
        return a
    if fa * fb > 0:
        # As a fallback, widen asymmetrically (very unlikely not to find a sign change for odd degree)
        # Try a few more expansions one-sided.
        for m in range(100):
            b *= 2.0
            fb = poly(xs, b)
            if fa * fb <= 0:
                break
        if fa * fb > 0:
            raise RuntimeError("Failed to bracket a root; input may violate the problem's guarantees.")

    # Standard bisection
    for _ in range(max_iter):
        mid = 0.5 * (a + b)
        fm = poly(xs, mid)
        if abs(fm) <= tol or abs(b - a) <= tol:
            return mid
        if fa * fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm

    return 0.5 * (a + b)  # return best midpoint if tolerance not reached