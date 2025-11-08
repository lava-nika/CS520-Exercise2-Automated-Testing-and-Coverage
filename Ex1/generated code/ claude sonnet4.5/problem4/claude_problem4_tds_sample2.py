def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''
    
    # Check progressively longer suffixes starting from position 0
    for split_pos in range(len(string)):
        suffix = string[split_pos:]
        if is_palindrome(suffix):
            # Found palindromic suffix
            # Append reverse of prefix
            return string + string[:split_pos][::-1]
    
    # Fallback (shouldn't reach here)
    return string

