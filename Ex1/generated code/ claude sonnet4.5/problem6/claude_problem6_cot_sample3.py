def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
    
    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    
    for bracket in brackets:
        if bracket == '(':
            # Opening bracket: push to stack
            stack.append('(')
        elif bracket == ')':
            # Closing bracket: try to match with opening
            if not stack:
                # No opening bracket to match with
                return False
            stack.pop()
    
    # Stack should be empty if all brackets are matched
    return len(stack) == 0

