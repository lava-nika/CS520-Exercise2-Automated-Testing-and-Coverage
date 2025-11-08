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

def poly(xs: List[float], x: float) -> float:
    """Evaluate polynomial using Horner's method (stable and fast)."""
    acc = 0.0
    # Highest-degree first
    for coeff in reversed(xs):
        acc = acc * x + coeff
    return acc

def find_zero(xs: List[float], tol: float = 1e-12, max_iter: int = 200) -> float:
    """
    Find one real root using the secant method (derivative-free).
    """
    xs = _validate_coeffs(xs)

    f = lambda t: poly(xs, t)

    x0 = 0.0
    f0 = f(x0)
    if abs(f0) <= tol:
        return x0

    # choose x1 and ensure f1 != f0 (avoid division by zero)
    x1 = 1.0
    f1 = f(x1)
    expand = 0
    while abs(f1 - f0) <= 1e-18 and expand < 100:
        x1 *= 2.0
        f1 = f(x1)
        expand += 1

    x_prev, x_curr = x0, x1
    f_prev, f_curr = f0, f1

    for _ in range(max_iter):
        denom = (f_curr - f_prev)
        if abs(denom) <= 1e-18:
            # Nudge current point slightly to avoid zero denominator
            x_curr += 1e-6 if x_curr == 0 else 1e-6 * (1 if x_curr > 0 else -1)
            f_curr = f(x_curr)
            denom = (f_curr - f_prev)
            if abs(denom) <= 1e-18:
                # As a last resort, change direction
                x_curr += 1e-3
                f_curr = f(x_curr)
                denom = (f_curr - f_prev)

        x_next = x_curr - f_curr * (x_curr - x_prev) / denom
        f_next = f(x_next)

        if abs(f_next) <= tol:
            return x_next

        x_prev, f_prev = x_curr, f_curr
        x_curr, f_curr = x_next, f_next

    # Best estimate after max_iter
    return x_curr
