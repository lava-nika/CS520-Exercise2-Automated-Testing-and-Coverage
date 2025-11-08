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


# -------- Implementation 2: Newton–Raphson (with derivative), damping & guardrails --------
def find_zero(xs: Optional[List[float]]):
    if xs is None:
        return None
    xs = [float(c) for c in xs]
    xs = _trim_trailing_zeros(xs)

    if len(xs) == 1 and xs[0] == 0.0:
        return 0.0
    if len(xs) == 1:
        return None

    # Evaluate polynomial and derivative via Horner
    def f(x: float) -> float:
        s = 0.0
        for c in reversed(xs):
            s = s * x + c
        return s

    def df(x: float) -> float:
        # derivative coefficients
        if len(xs) <= 1:
            return 0.0
        s = 0.0
        for c in reversed(xs[1:]):
            s = s * x + c
        return s

    # Cauchy bound
    an = xs[-1]
    R = 1.0 + max((abs(c / an) for c in xs[:-1]), default=0.0)

    # Try a few initial guesses
    initials = [0.0, 1.0, -1.0, R / 2.0, -R / 2.0]
    for x0 in initials:
        y0 = f(x0)
        if y0 == 0.0:
            return x0

    x = 0.0
    for _ in range(5):  # attempt multiple restarts if needed
        x = initials[_]
        for _iter in range(100):
            fx = f(x)
            dfx = df(x)
            if fx == 0.0:
                return x
            if dfx == 0.0 or not math.isfinite(dfx):
                x += 1.0  # nudge
                continue
            step = fx / dfx
            # damping if step is too large
            lam = 1.0
            xn = x - lam * step
            # If it diverges wildly, damp
            tries = 0
            while tries < 5 and (not math.isfinite(xn) or abs(xn) > 10 * (R + 1)):
                lam *= 0.5
                xn = x - lam * step
                tries += 1
            x = xn
            if not math.isfinite(x):
                break
            if abs(fx) < 1e-12 and abs(step) < 1e-12:
                return x
    # As a last small sweep, check a coarse grid for exact zero
    for probe in (-R, -R/2, 0.0, R/2, R):
        if f(probe) == 0.0:
            return probe
    return None  # give up (likely no real root)