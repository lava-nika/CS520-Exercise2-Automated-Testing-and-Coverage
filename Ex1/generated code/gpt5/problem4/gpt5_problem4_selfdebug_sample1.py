def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.

    Algorithm:
      - Find the longest suffix of the string that is already a palindrome.
      - Append to the end of the string the reverse of the prefix before that suffix.

    Examples
    --------
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not isinstance(string, str):
        raise TypeError("make_palindrome expects a string input")

    def is_palindrome(s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    n = len(string)
    # Scan from the full string down by moving the start index forward.
    # The first palindromic suffix we find is the longest.
    for i in range(n + 1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    # Should never reach here (empty suffix is always a palindrome), but keep a fallback.
    return string
