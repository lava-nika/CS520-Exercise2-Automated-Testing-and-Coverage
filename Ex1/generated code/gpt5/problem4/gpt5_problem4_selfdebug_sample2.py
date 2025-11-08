from typing import List

def _is_pal(s: str) -> bool:
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """
    Find the longest palindromic suffix by scanning, then append the reverse
    of the prefix that precedes it. O(n^2) in the worst case.
    """
    if not isinstance(string, str):
        raise TypeError("make_palindrome expects a str")

    n = len(string)
    if n <= 1 or _is_pal(string):
        return string

    # Find smallest i such that string[i:] is a palindrome -> longest palindromic suffix
    for i in range(n):
        if _is_pal(string[i:]):
            return string + string[:i][::-1]

    # Should never be reached (last char alone is a palindrome)
    return string + string[:-1][::-1]