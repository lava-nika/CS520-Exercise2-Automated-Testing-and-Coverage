def correct_bracketing(brackets: str) -> bool:
    """Return True if the parentheses string is well-formed.

    The sequence is correct if no prefix has more ')' than '('
    and the total number of '(' equals the number of ')'.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    >>> correct_bracketing("")
    True
    """
    balance = 0
    for ch in brackets:
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            balance -= 1
            if balance < 0:
                return False
    return balance == 0
