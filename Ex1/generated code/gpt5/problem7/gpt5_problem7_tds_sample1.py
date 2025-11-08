from typing import Iterable, Optional, List

def _normalize_arr(arr: Optional[Iterable[object]]) -> List[int]:
    """Normalize arr to a list of integers, ignoring non-int (and non-bool) entries.
       Treat None as empty."""
    if arr is None:
        return []
    out: List[int] = []
    for x in arr:
        if isinstance(x, bool):
            # Treat booleans as non-integers for this problem to avoid True==1 confusion
            continue
        if isinstance(x, int):
            out.append(x)
        # ignore other types silently
    return out


# Helper: signed-digit sum
def _signed_digit_sum_math(n: int) -> int:
    """Compute sum of digits with only the first digit of a negative number being negative."""
    if n == 0:
        return 0
    if n > 0:
        s = 0
        while n:
            n, d = divmod(n, 10)
            s += d
        return s
    # n < 0
    m = -n
    # find first digit of m
    first = 0
    while m >= 10:
        m //= 10
    first = m
    # sum of absolute digits of -n
    m = -n
    s_abs = 0
    while m:
        m, d = divmod(m, 10)
        s_abs += d
    return s_abs - 2 * first  # convert first digit from +first to -first

# Implementation 1: Pure math digit extraction (no strings)
def count_nums(arr: Optional[Iterable[object]]) -> int:
    items = _normalize_arr(arr)
    cnt = 0
    for n in items:
        if _signed_digit_sum_math(n) > 0:
            cnt += 1
    return cnt