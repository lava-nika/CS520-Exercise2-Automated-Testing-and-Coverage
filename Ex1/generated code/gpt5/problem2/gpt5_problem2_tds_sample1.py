from typing import List, Optional
import itertools

def _clean(s: Optional[str]) -> str:
    """Remove spaces; normalize None to empty string."""
    if not s:
        return ''
    return ''.join(ch for ch in s if ch != ' ')

# Approach 1: Counter with slicing via indices (using accumulate on +1/-1)
def separate_paren_groups(paren_string: Optional[str]) -> List[str]:
    s = _clean(paren_string)
    if not s:
        return []
    # Balance counter: '(' -> +1, ')' -> -1
    balance_changes = [1 if c == '(' else -1 for c in s]
    # Running balance
    running = list(itertools.accumulate(balance_changes, initial=0))[1:]
    groups: List[str] = []
    start = 0
    for i, b in enumerate(running):
        if b == 0:
            groups.append(s[start:i+1])
            start = i + 1
    # If input is guaranteed balanced at top-level, start should end at len(s)
    return groups