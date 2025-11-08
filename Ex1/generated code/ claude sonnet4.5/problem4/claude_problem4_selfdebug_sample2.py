def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    """
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    if not string:
        return ''
    
    if is_palindrome(string):
        return string
    
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            prefix = string[:i]
            return string + prefix[::-1]
    
    return string

