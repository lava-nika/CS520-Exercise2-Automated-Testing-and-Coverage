from typing import Optional, Iterable

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure str."""
    if s is None:
        return ''
    return s

# Implementation 1: Direct set equality
def same_chars(s0: Optional[str], s1: Optional[str]) -> bool:
    a = set(_normalize(s0))
    b = set(_normalize(s1))
    return a == b