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
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    # Edge case: empty string is already a palindrome
    if not string:
        return ''
    
    # Find the longest suffix that is a palindrome
    # Start checking from the full string (i=0) and move right
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            # Found palindromic suffix starting at index i
            # Prefix that needs to be reversed is string[:i]
            prefix = string[:i]
            return string + prefix[::-1]
    
    # Unreachable: at minimum, last character is always a palindrome
    return string