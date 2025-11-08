def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string.

    Algorithm:
      - Find the longest suffix of the string that is a palindrome.
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
    def is_palindrome(s: str) -> bool:
        """Check palindrome with a two-pointer scan."""
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    n = len(string)
    # Scan for the longest palindromic suffix: string[i:] being a palindrome
    for i in range(n + 1):
        if is_palindrome(string[i:]):
            # Append reverse of the prefix before this suffix
            return string + string[:i][::-1]

    # The loop always returns; this is just a safety fallback.
    return string
