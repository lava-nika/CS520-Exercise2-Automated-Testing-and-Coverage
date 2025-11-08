from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    
    if not paren_string:
        return []
    
    result = []
    current_group = []
    depth = 0
    
    for char in paren_string:
        if char == '(':
            current_group.append(char)
            depth += 1
        elif char == ')':
            current_group.append(char)
            depth -= 1
            
            if depth == 0:
                result.append(''.join(current_group))
                current_group = []
    
    return result

