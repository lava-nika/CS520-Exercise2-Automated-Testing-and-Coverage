from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    result = []
    current_group = []
    balance = 0
    
    for char in paren_string:
        if char == ' ':
            continue
        
        if char == '(':
            current_group.append(char)
            balance += 1
        elif char == ')':
            current_group.append(char)
            balance -= 1
            
            if balance == 0:
                result.append(''.join(current_group))
                current_group = []
    
    return result

