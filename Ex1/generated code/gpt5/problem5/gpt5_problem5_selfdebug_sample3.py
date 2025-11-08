from typing import Iterable

def _ensure_strs(s0, s1):
    if not isinstance(s0, str) or not isinstance(s1, str):
        raise TypeError("same_chars expects two strings")

def same_chars(s0: str, s1: str) -> bool:
    _ensure_strs(s0, s1)
    # dict.fromkeys removes duplicates while keeping order; then sort
    u0 = sorted(dict.fromkeys(s0))
    u1 = sorted(dict.fromkeys(s1))
    return u0 == u1