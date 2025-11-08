def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return sorted(set(s0)) == sorted(set(s1))

