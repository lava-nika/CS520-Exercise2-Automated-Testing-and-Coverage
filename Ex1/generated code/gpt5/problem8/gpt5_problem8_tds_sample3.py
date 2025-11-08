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


# -------- Implementation 3: Secant Method with adaptive initials --------
def find_zero(xs: Optional[List[float]]):
    if xs is None:
        return None
    xs = [float(c) for c in xs]
    xs = _trim_trailing_zeros(xs)

    if len(xs) == 1 and xs[0] == 0.0:
        return 0.0
    if len(xs) == 1:
        return None

    def f(x: float) -> float:
        s = 0.0
        p = 1.0
        for c in xs:
            s += c * p
            p *= x
        return s

    # Cauchy bound
    an = xs[-1]
    R = 1.0 + max((abs(c / an) for c in xs[:-1]), default=0.0)

    # Initial guesses
    x0, x1 = -R if math.isfinite(R) else -1.0, R if math.isfinite(R) else 1.0
    f0, f1 = f(x0), f(x1)
    # If endpoints are roots
    if f0 == 0.0:
        return x0
    if f1 == 0.0:
        return x1
    # If both same sign, tweak x1
    if f0 * f1 > 0:
        x1 = 0.0
        f1 = f(x1)
        if f1 == 0.0:
            return x1

    # Secant iterations
    for _ in range(200):
        if f1 == f0:
            # reset guesses a bit
            x0, x1 = x1, x1 + 1.0
            f0, f1 = f1, f(x1)
            continue
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if not math.isfinite(x2) or abs(x2) > 10 * (R + 1):
            # fallback jiggle
            x2 = (x1 + x0) / 2.0
        f2 = f(x2)
        if f2 == 0.0 or abs(x2 - x1) < 1e-12:
            return x2
        x0, f0, x1, f1 = x1, f1, x2, f2
    return x1  # best effort