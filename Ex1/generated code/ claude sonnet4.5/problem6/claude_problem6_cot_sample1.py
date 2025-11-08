def correct_bracketing(brackets: str):
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
    balance = 0
    
    for bracket in brackets:
        if bracket == "(":
            balance += 1
        elif bracket == ")":
            balance -= 1
        
        # If balance goes negative, we have a closing bracket 
        # without a matching opening bracket
        if balance < 0:
            return False
    
    # All brackets must be matched (balance should be 0)
    return balance == 0