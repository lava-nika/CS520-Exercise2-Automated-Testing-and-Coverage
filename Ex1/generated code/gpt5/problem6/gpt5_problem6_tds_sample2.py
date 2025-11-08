from typing import Optional

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure only '(' and ')' are considered."""
    if s is None:
        return ""
    return s

# Implementation 2: Explicit stack push/pop (O(n), O(n) worst-case space)
def correct_bracketing(brackets: Optional[str]) -> bool:
    s = _normalize(brackets)
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
        else:
            continue
    return not stack