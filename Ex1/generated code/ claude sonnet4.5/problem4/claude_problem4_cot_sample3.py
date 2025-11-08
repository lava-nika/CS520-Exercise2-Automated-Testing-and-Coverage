def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Helper to check palindrome
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    # Handle empty string
    if len(string) == 0:
        return ''
    
    # Try each possible split point
    # i represents where the palindromic suffix starts
    for i in range(len(string) + 1):
        # Check if the suffix starting at position i is a palindrome
        if is_palindrome(string[i:]):
            # We found the longest palindromic suffix
            # Append the reverse of the prefix (before position i)
            return string + string[:i][::-1]
    
    # Should never reach here
    return string

