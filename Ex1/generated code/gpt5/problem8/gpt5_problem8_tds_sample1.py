import math
from typing import List, Optional

# -------- Utility: trimming and validation --------
def _trim_trailing_zeros(xs: List[float]) -> List[float]:
    if not xs:
        return []
    i = len(xs) - 1
    while i >= 0 and xs[i] == 0:
        i -= 1
    return xs[: i + 1] if i >= 0 else [0.0]

# -------- Implementation 1: Robust Bisection with automatic bracketing --------
def find_zero(xs: Optional[List[float]]):
    if xs is None:
        return None
    xs = [float(c) for c in xs]
    xs = _trim_trailing_zeros(xs)

    # Zero polynomial -> any x; return 0.0
    if len(xs) == 1 and xs[0] == 0.0:
        return 0.0
    # Constant nonzero -> no real root
    if len(xs) == 1:
        return None

    # Local poly evaluator
    def f(x: float) -> float:
        s = 0.0
        p = 1.0
        for c in xs:
            s += c * p
            p *= x
        return s

    # Quick exact zero checks at a few points
    for probe in (0.0, 1.0, -1.0):
        val = f(probe)
        if val == 0.0:
            return probe

    # Compute a Cauchy bound for roots: R = 1 + max |a_i / a_n|
    an = xs[-1]
    if an == 0:
        return None  # shouldn't happen due to trimming
    R = 1.0 + max((abs(c / an) for c in xs[:-1]), default=0.0)

    # Try to find a sign-changing bracket by expanding range
    def find_bracket() -> Optional[tuple[float, float]]:
        L = 1.0
        # Expand up to some iterations
        for _ in range(30):
            a, b = -L * R, L * R
            fa, fb = f(a), f(b)
            if fa == 0.0:
                return (a, a)
            if fb == 0.0:
                return (b, b)
            if fa * fb < 0:
                return (a, b)
            # Scan grid inside [a,b] for adjacent sign change
            steps = 50
            x_prev, f_prev = a, fa
            for k in range(1, steps + 1):
                xk = a + (b - a) * k / steps
                fk = f(xk)
                if fk == 0.0:
                    return (xk, xk)
                if f_prev * fk < 0:
                    return (x_prev, xk)
                x_prev, f_prev = xk, fk
            L *= 2.0
        return None

    bracket = find_bracket()
    if bracket is None:
        # Could be no real roots (e.g., x^2+1)
        return None
    a, b = bracket
    if a == b:
        return a

    fa, fb = f(a), f(b)
    # Bisection
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = f(m)
        if fm == 0.0 or abs(b - a) < 1e-12:
            return m
        # Decide side
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)