def correct_bracketing(brackets: str):
    open_count = 0
    
    for bracket in brackets:
        if bracket == '(':
            open_count += 1
        elif bracket == ')':
            open_count -= 1
            if open_count < 0:
                return False
    
    return open_count == 0

