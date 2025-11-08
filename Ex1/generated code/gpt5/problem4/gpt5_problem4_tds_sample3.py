from typing import List, Optional

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure str."""
    if s is None:
        return ''
    return s

def _is_pal(s: str) -> bool:
    return s == s[::-1]

# Approach 3: Manacher’s algorithm to get longest palindromic suffix in O(n)
def make_palindrome(string: Optional[str]) -> str:
    s = _normalize(string)
    n = len(s)
    if n <= 1:
        return s

    # Odd-length pal radii: d1[i] is radius such that s[i - d1[i] + 1 .. i + d1[i] - 1] is palindrome
    d1 = [0] * n
    l = r = -1
    for i in range(n):
        k = 1 if i > r else min(d1[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
            k += 1
        d1[i] = k
        k -= 1
        if i + k > r:
            l, r = i - k, i + k

    # Even-length pal radii: d2[i] is radius such that s[i - d2[i] .. i + d2[i] - 1] is palindrome
    d2 = [0] * n
    l = r = -1
    for i in range(n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        k -= 1
        if i + k > r:
            l, r = i - k - 1, i + k

    # Find the longest palindrome that ends at the last index (n-1)
    max_len = 1
    start_idx = n - 1

    # Check odd centers
    for i in range(n):
        radius = d1[i]
        end = i + radius - 1
        if end == n - 1:
            length = 2 * radius - 1
            if length > max_len:
                max_len = length
                start_idx = i - radius + 1

    # Check even centers
    for i in range(n):
        radius = d2[i]
        end = i + radius - 1
        if end == n - 1 and radius > 0:
            length = 2 * radius
            if length > max_len:
                max_len = length
                start_idx = i - radius

    # start_idx gives start of longest palindromic suffix (length max_len)
    i = start_idx
    if i < 0:  # safety
        i = 0
    return s + s[:i][::-1]