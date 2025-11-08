from typing import Optional

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure only '(' and ')' are considered."""
    if s is None:
        return ""
    return s

# Implementation 1: Single pass counter with early-fail (O(n), O(1) space)
def correct_bracketing(brackets: Optional[str]) -> bool:
    s = _normalize(brackets)
    bal = 0
    for ch in s:
        if ch == "(":
            bal += 1
        elif ch == ")":
            bal -= 1
            if bal < 0:
                return False
        else:
            # Spec says input is only '(' and ')'; ignore others if any appear
            continue
    return bal == 0