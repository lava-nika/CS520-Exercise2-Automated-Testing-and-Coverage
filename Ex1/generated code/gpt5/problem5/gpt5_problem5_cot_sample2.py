def same_chars(s0: str, s1: str) -> bool:
    """
    Solution A: use Python set equality on character sets.
    """
    return set(s0) == set(s1)