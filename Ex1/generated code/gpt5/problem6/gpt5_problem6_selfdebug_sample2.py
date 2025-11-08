def correct_bracketing(brackets: str) -> bool:
    """
    Solution A: Single-pass balance counter with early failure.
    Returns True iff parentheses are balanced and properly ordered.
    """
    bal = 0
    for ch in brackets:
        if ch == '(':
            bal += 1
        elif ch == ')':
            bal -= 1
            if bal < 0:  # close without a prior open
                return False
        else:
            raise ValueError("Input must contain only '(' and ')'.")
    return bal == 0