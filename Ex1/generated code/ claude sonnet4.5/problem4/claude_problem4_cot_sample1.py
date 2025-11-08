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
    # Helper function to check if a string is a palindrome
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    # Edge case: empty string is already a palindrome
    if not string:
        return ''
    
    # Try to find the longest suffix that is a palindrome
    # Start with the full string and work backwards
    for i in range(len(string)):
        # Check if string[i:] is a palindrome
        if is_palindrome(string[i:]):
            # Found the longest palindromic suffix
            # The prefix is string[0:i]
            # Append reverse of prefix to the original string
            prefix = string[:i]
            return string + prefix[::-1]
    
    # This should never be reached (at minimum, last char is a palindrome)
    return string