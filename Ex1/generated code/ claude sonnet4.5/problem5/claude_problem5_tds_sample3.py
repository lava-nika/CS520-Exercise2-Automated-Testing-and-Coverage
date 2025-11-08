def same_chars(s0: str, s1: str):
    unique_s0 = sorted(set(s0))
    unique_s1 = sorted(set(s1))
    return unique_s0 == unique_s1

