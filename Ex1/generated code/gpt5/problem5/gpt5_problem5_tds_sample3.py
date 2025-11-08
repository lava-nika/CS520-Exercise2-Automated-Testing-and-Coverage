from typing import Optional, Iterable

def _normalize(s: Optional[str]) -> str:
    """Normalize None to empty string; ensure str."""
    if s is None:
        return ''
    return s

# Implementation 3: Build unique-char collections without Python set literals (manual)
def _unique_chars(iterable: Iterable[str]) -> dict:
    """Return a dict of seen chars as keys (values unused), emulating a set."""
    seen = {}
    for ch in iterable:
        if ch not in seen:
            seen[ch] = True
    return seen

def same_chars(s0: Optional[str], s1: Optional[str]) -> bool:
    a = _unique_chars(_normalize(s0))
    b = _unique_chars(_normalize(s1))
    # Compare keys as frozensets to avoid constructing intermediate Python sets in loop
    return frozenset(a.keys()) == frozenset(b.keys())