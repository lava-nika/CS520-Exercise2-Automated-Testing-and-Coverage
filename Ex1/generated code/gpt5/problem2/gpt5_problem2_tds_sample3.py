from typing import List, Optional
import itertools

def _clean(s: Optional[str]) -> str:
    """Remove spaces; normalize None to empty string."""
    if not s:
        return ''
    return ''.join(ch for ch in s if ch != ' ')

# Approach 3: Recursive peel-first-group then recurse remainder
def separate_paren_groups(paren_string: Optional[str]) -> List[str]:
    s = _clean(paren_string)
    if not s:
        return []
    def split_first(rest: str) -> (str, str):
        """Return (first_group, remaining) assuming rest begins with '(' and groups are balanced."""
        depth = 0
        for i, ch in enumerate(rest):
            if ch == '(':
                depth += 1
            else:  # ')'
                depth -= 1
                if depth == 0:
                    return rest[:i+1], rest[i+1:]
        return rest, ''  # fallback; spec says balanced so we shouldn't get here

    groups: List[str] = []
    while s:
        g, s = split_first(s)
        groups.append(g)
    return groups