from typing import List, Optional, Iterable
import heapq

_NAMES = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
}

def _normalize(arr: Optional[Iterable[object]]) -> List[int]:
    """Keep only true ints in [1,9]; ignore bools and everything else."""
    if arr is None:
        return []
    out: List[int] = []
    for x in arr:
        # exclude bool (subclass of int) explicitly
        if isinstance(x, bool):
            continue
        if isinstance(x, int) and 1 <= x <= 9:
            out.append(x)
    return out

# Implementation 1: Sort + map (straightforward)
def by_length(arr: Optional[Iterable[object]]) -> List[str]:
    vals = _normalize(arr)
    vals.sort(reverse=True)  # descending after sorting ascending+reverse
    return [_NAMES[v] for v in vals]
