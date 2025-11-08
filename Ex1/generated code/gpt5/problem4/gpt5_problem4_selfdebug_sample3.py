from typing import List

def _is_pal(s: str) -> bool:
    return s == s[::-1]

def _pick_sentinel(s: str) -> str:
    """
    Choose a separator character not appearing in s to avoid false matches in KMP.
    Tries a small set; falls back to a rare control char.
    """
    for ch in ('#', '$', '@', '\x00', '\x01', '\x02', '|', '^'):
        if ch not in s:
            return ch
    # Extremely unlikely fallback: try a character outside BMP if not present.
    # If s already contains it, correctness is still fine but less guaranteed;
    # in practice the tries above suffice.
    exotic = '\uFFFF'
    if exotic not in s:
        return exotic
    return '\x03'

def _kmp_lps(pattern: str) -> List[int]:
    """
    Build LPS (Longest Prefix Suffix) array for KMP in O(n).
    lps[i] = length of the longest proper prefix of pattern[:i+1]
             which is also a suffix of pattern[:i+1].
    """
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def make_palindrome(string: str) -> str:
    """
    Use KMP to compute the length L of the longest palindromic suffix in O(n).
    Then append reverse(string[:n-L]).
    """
    if not isinstance(string, str):
        raise TypeError("make_palindrome expects a str")

    s = string
    n = len(s)
    if n <= 1 or _is_pal(s):
        return s

    rs = s[::-1]
    sep = _pick_sentinel(s)
    # Construct T = reverse(s) + sep + s
    T = rs + sep + s
    lps = _kmp_lps(T)
    L = lps[-1]  # length of the longest prefix of reverse(s) matching a suffix of s
    # That L is exactly the length of the longest palindromic suffix of s
    return s + s[:n - L][::-1]