def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    """
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    if len(string) == 0:
        return ''
    
    for i in range(len(string) + 1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    
    return string

