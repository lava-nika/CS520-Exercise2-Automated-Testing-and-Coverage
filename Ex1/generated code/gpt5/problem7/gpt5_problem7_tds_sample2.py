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

# Implementation 2: String-based parsing of signed digits
def count_nums(arr: Optional[Iterable[object]]) -> int:
    items = _normalize_arr(arr)
    def signed_sum(n: int) -> int:
        s = str(n)
        if s[0] != '-':
            return sum(int(ch) for ch in s)
        # negative: first signed digit negative
        if len(s) == 2:  # "-d"
            return -int(s[1])
        total = -int(s[1]) + sum(int(ch) for ch in s[2:])
        return total
    return sum(1 for n in items if signed_sum(n) > 0)