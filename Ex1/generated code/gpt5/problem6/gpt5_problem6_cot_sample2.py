def correct_bracketing(brackets: str) -> bool:
    """
    Solution A: one-pass counter with early failure.
    Returns True iff parentheses are balanced and properly ordered.
    """
    bal = 0
    for ch in brackets:
        if ch == '(':
            bal += 1
        elif ch == ')':
            bal -= 1
            if bal < 0:  # a close without a prior open
                return False
        else:
            # If inputs can contain only '(' and ')', you could also raise.
            # We'll treat any other char as invalid.
            raise ValueError("Input must contain only '(' and ')'.")
    return bal == 0