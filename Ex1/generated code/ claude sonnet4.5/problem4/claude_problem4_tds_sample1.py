def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''
    
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            prefix = string[:i]
            return string + prefix[::-1]
    
    return string

