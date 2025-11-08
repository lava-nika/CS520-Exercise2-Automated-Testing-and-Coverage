def correct_bracketing(brackets: str) -> bool:
    """Return True if every '(' has a corresponding ')' in the correct order.

    The sequence is correct iff no prefix has more ')' than '(' and the final balance is zero.

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
    if not isinstance(brackets, str):
        raise TypeError("correct_bracketing expects a string")

    balance = 0
    for ch in brackets:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance < 0:
                return False
        else:
            raise ValueError("Input must contain only '(' and ')' characters")

    return balance == 0
