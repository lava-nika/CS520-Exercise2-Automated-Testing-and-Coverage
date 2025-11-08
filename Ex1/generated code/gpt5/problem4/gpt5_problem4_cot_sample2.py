from typing import List

def _is_pal(s: str) -> bool:
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """
    Find the longest palindromic suffix by scanning, then append the reverse
    of the prefix that precedes it. O(n^2) in the worst case.
    """
    n = len(string)
    if n <= 1 or _is_pal(string):
        return string

    # Find smallest i such that string[i:] is a palindrome (=> longest pal suffix)
    for i in range(n):
        if _is_pal(string[i:]):
            # Append reverse of the prefix before that suffix
            return string + string[:i][::-1]
    # Fallback (should never hit due to i= n-1 giving a 1-char palindrome)
    return string + string[:-1][::-1]