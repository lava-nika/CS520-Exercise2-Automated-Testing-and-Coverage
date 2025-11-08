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
    """Evaluate polynomial using Horner's method (stable and fast)."""
    acc = 0.0
    for coeff in reversed(xs):
        acc = acc * x + coeff
    return acc


def _derivative_coeffs(xs: List[float]) -> List[float]:
    """Return coefficients of the derivative polynomial, ascending powers."""
    if len(xs) <= 1:
        return [0.0]
    return [i * xs[i] for i in range(1, len(xs))]

def find_zero(xs: List[float], tol: float = 1e-12, max_iter: int = 100) -> float:
    """
    Find one real root using Newton's method with simple damping.
    """
    xs = _validate_coeffs(xs)

    # Build derivative coefficients
    dxs = _derivative_coeffs(xs)

    # Use Horner for robustness
    f = lambda t: poly(xs, t)
    fp = lambda t: poly(dxs, t)

    # Early out if 0 is a root
    f0 = f(0.0)
    if abs(f0) <= tol:
        return 0.0

    x = 0.0
    # If derivative at start is zero, nudge the initial guess
    if abs(fp(x)) < 1e-18:
        x = 1.0

    prev_val = abs(f(x))
    for _ in range(max_iter):
        fx = f(x)
        dfx = fp(x)
        if abs(fx) <= tol:
            return x
        if abs(dfx) < 1e-18:
            # Derivative too small -> nudge x
            x += 1e-3 if x >= 0 else -1e-3
            continue

        step = fx / dfx
        x_new = x - step

        # Simple damping: if not improving, shrink the step
        f_new = f(x_new)
        if abs(f_new) > prev_val:
            # try halving step a few times
            damp = 0
            while abs(f_new) > prev_val and damp < 10:
                step *= 0.5
                x_new = x - step
                f_new = f(x_new)
                damp += 1

        x, prev_val = x_new, abs(f_new)

        if prev_val <= tol:
            return x

    # Last estimate if tolerance not met
    return x
