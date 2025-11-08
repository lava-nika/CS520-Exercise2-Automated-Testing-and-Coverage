from typing import List, Optional

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure str."""
    if s is None:
        return ''
    return s

def _is_pal(s: str) -> bool:
    return s == s[::-1]

# Approach 1: Naive scan — check each suffix via slicing (O(n^2) worst-case)
def make_palindrome(string: Optional[str]) -> str:
    s = _normalize(string)
    n = len(s)
    # Find the smallest i such that s[i:] is a palindrome
    for i in range(n):
        if _is_pal(s[i:]):
            # Append reverse of the prefix before i
            return s + s[:i][::-1]
    # If s is empty, loop won't run; return s
    return s