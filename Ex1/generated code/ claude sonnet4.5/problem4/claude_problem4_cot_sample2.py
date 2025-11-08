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
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    # Empty string is already a palindrome
    if not string:
        return ''
    
    # Check if the entire string is already a palindrome
    if is_palindrome(string):
        return string
    
    # Find the longest suffix that is a palindrome
    # Start from the full string and work backwards
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Found the longest palindromic suffix
            # The prefix is everything before this suffix
            prefix = string[:i]
            # Append the reverse of the prefix to make a palindrome
            return string + prefix[::-1]
    
    # This line should never be reached because at minimum,
    # the last character is always a palindrome
    return string

