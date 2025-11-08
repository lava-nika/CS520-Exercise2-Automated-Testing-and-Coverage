from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    
    if not paren_string:
        return []
    
    result = []
    stack = []
    start_index = 0
    
    for i, char in enumerate(paren_string):
        if char == '(':
            if not stack:
                start_index = i
            stack.append(char)
        elif char == ')':
            stack.pop()
            if not stack:
                result.append(paren_string[start_index:i+1])
    
    return result

