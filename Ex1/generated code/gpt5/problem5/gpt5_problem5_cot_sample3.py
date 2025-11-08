from typing import Iterable

def same_chars(s0: str, s1: str) -> bool:
    """
    Solution B: build presence maps (dicts) by scanning once, then compare keys.
    Avoids constructing Python sets directly (functionally equivalent).
    """
    def presence(s: str) -> dict[str, bool]:
        seen: dict[str, bool] = {}
        for ch in s:
            # Mark presence; repeated writes are harmless
            seen[ch] = True
        return seen

    p0 = presence(s0)
    p1 = presence(s1)
    # Compare the exact same keys (i.e., same unique characters)
    if len(p0) != len(p1):
        return False
    # Compare membership both ways without converting to set (keeps approach distinct)
    for ch in p0:
        if ch not in p1:
            return False
    return True