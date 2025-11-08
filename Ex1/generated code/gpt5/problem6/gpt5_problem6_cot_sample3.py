def correct_bracketing(brackets: str) -> bool:
    """
    Solution B: repeatedly remove '()' pairs until none remain.
    If the string is empty at the end, it's balanced.
    """
    # Simple validation (optional if the problem guarantees only '(' and ')')
    if any(ch not in '()' for ch in brackets):
        raise ValueError("Input must contain only '(' and ')'.")
    s = brackets
    # Repeatedly eliminate matched pairs
    while '()' in s:
        s = s.replace('()', '')
    return s == ''