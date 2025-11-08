import math
from typing import List, Tuple

# ----------------------------- Helpers & Validation -----------------------------

def _trim_trailing_zeros(xs: List[float]) -> List[float]:
    """Remove trailing zeros so the highest-degree term is nonzero, if possible."""
    if not xs:
        return xs
    i = len(xs) - 1
    while i >= 0 and xs[i] == 0:
        i -= 1
    return xs[:i + 1]

def _validate_coeffs(xs: List[float]) -> List[float]:
    xs = _trim_trailing_zeros(xs)
    if not xs:
        raise ValueError("Polynomial is empty or identically zero.")
    if len(xs) % 2 != 0:
        raise ValueError("xs must contain an even number of coefficients (odd degree after trimming).")
    # highest-degree coefficient is non-zero by trimming
    return xs


def poly(xs: List[float], x: float) -> float:
    """Evaluate polynomial with sum of powers (uses math.pow)."""
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def _bracket_root(xs: List[float], f, start_a=-1.0, start_b=1.0, expand_limit=100) -> Tuple[float, float]:
    """Find [a,b] with f(a)*f(b) <= 0 by exponential expansion."""
    a, b = float(start_a), float(start_b)
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return a, a
    if fb == 0.0:
        return b, b
    k = 0
    while fa * fb > 0 and k < expand_limit:
        a *= 2.0
        b *= 2.0
        fa, fb = f(a), f(b)
        k += 1
    return a, b

def find_zero(xs: List[float], tol: float = 1e-12, max_iter: int = 200) -> float:
    """
    Find one real root using bracketing + bisection (robust).
    """
    xs = _validate_coeffs(xs)
    f = lambda t: poly(xs, t)

    f0 = f(0.0)
    if abs(f0) <= tol:
        return 0.0

    a, b = _bracket_root(xs, f)
    if a == b:                   # exact root at endpoint
        return a
    fa, fb = f(a), f(b)

    if fa * fb > 0:
        # As a last resort, try asymmetric expansion further (extremely unlikely to fail for odd degree).
        for _ in range(200):
            b *= 2.0
            fb = f(b)
            if fa * fb <= 0:
                break
        if fa * fb > 0:
            raise RuntimeError("Failed to bracket a root; input may violate the problem's guarantees.")

    # Standard bisection loop
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        fm = f(m)
        if abs(fm) <= tol or abs(b - a) <= tol:
            return m
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)  # best midpoint
