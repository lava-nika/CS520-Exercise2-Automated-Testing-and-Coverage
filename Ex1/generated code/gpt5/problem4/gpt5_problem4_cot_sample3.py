from typing import List

def _kmp_lps(pattern: str) -> List[int]:
    """
    Build LPS (longest prefix-suffix) array for KMP in O(n).
    lps[i] = length of the longest proper prefix of pattern[:i+1]
             which is also a suffix of pattern[:i+1]
    """
    lps = [0] * len(pattern)
    j = 0  # length of current longest prefix
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def make_palindrome(string: str) -> str:
    """
    Use the standard trick: longest palindromic prefix of X is lps of X + '#' + reverse(X).
    Here X = reverse(string) so we actually get the longest palindromic suffix of 'string'.
    Overall O(n).
    """
    s = string
    n = len(s)
    if n <= 1 or s == s[::-1]:
        return s

    X = s[::-1]               # reverse(s)
    T = X + "#" + X[::-1]     # reverse(s) + '#' + s
    lps = _kmp_lps(T)
    L = lps[-1]               # length of longest palindromic suffix of s

    # Append reverse of the prefix before that suffix
    return s + s[:n - L][::-1]