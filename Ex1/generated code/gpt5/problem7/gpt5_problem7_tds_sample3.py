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

# Implementation 3: Hybrid formula using sum(abs digits) and first digit (fast)
def count_nums(arr: Optional[Iterable[object]]) -> int:
    items = _normalize_arr(arr)
    def first_digit_abs(x: int) -> int:
        x = abs(x)
        if x == 0:
            return 0
        while x >= 10:
            x //= 10
        return x
    def sum_abs_digits(x: int) -> int:
        x = abs(x)
        s = 0
        while x:
            x, d = divmod(x, 10)
            s += d
        return s
    cnt = 0
    for n in items:
        if n >= 0:
            s = sum_abs_digits(n)  # same as signed
        else:
            s = sum_abs_digits(n) - 2 * first_digit_abs(n)
        if s > 0:
            cnt += 1
    return cnt