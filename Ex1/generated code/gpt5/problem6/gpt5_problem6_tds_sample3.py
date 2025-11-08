from typing import Optional

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure only '(' and ')' are considered."""
    if s is None:
        return ""
    return s

# Implementation 3: Iterative reduction by removing "()" pairs (O(k*n) worst-case)
def correct_bracketing(brackets: Optional[str]) -> bool:
    s = _normalize(brackets)
    # Quick parity check: odd length can't be balanced
    if len(s) % 2 == 1:
        # still need to handle cases like None->"" (already even/zero)
        return False if s else True
    # Repeatedly remove "()" until no more can be removed
    prev_len = -1
    while prev_len != len(s):
        prev_len = len(s)
        s = s.replace("()", "")
    return s == ""