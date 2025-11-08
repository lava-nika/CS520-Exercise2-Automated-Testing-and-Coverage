def correct_bracketing(brackets: str) -> bool:
    """
    Solution B: Repeatedly remove '()' pairs until none remain.
    If the string is empty at the end, it's balanced.
    """
    if any(ch not in '()' for ch in brackets):
        raise ValueError("Input must contain only '(' and ')'.")
    s = brackets
    while '()' in s:
        s = s.replace('()', '')
    return s == ''