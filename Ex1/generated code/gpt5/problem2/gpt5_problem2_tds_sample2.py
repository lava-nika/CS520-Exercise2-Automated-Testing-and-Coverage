from typing import List, Optional
import itertools

def _clean(s: Optional[str]) -> str:
    """Remove spaces; normalize None to empty string."""
    if not s:
        return ''
    return ''.join(ch for ch in s if ch != ' ')

# Approach 2: Stream builder with current buffer
def separate_paren_groups(paren_string: Optional[str]) -> List[str]:
    s = _clean(paren_string)
    if not s:
        return []
    groups: List[str] = []
    buf: List[str] = []
    depth = 0
    for ch in s:
        if ch == '(':
            depth += 1
            buf.append(ch)
        elif ch == ')':
            buf.append(ch)
            depth -= 1
            if depth == 0:
                groups.append(''.join(buf))
                buf.clear()
        else:
            # Ignore any unexpected non-parenthesis (not expected per spec)
            pass
    return groups