from typing import List, Optional

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure str."""
    if s is None:
        return ''
    return s

def _is_pal(s: str) -> bool:
    return s == s[::-1]

# Approach 2: Two-pointer palindrome check per candidate suffix (still O(n^2), less slicing)
def make_palindrome(string: Optional[str]) -> str:
    s = _normalize(string)
    n = len(s)

    def is_pal_suffix(start: int) -> bool:
        i, j = start, n - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    for i in range(n):
        if is_pal_suffix(i):
            return s + s[:i][::-1]
    return s