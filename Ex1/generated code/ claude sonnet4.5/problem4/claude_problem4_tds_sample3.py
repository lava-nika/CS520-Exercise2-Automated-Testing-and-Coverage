def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''
    
    if is_palindrome(string):
        return string
    
    for i in range(1, len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    
    return string + string[:-1][::-1]

