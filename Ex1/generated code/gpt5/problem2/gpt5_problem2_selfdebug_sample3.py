from typing import List
import math

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Solution B: Remove spaces, then slice by balance.
    """
    s = ''.join(ch for ch in paren_string if ch != ' ')
    if any(ch not in '()' for ch in s):
        bad = next(ch for ch in s if ch not in '()')
        raise ValueError(f"Unexpected character {bad!r}. Only '(' and ')' are allowed (spaces ignored).")

    groups: List[str] = []
    balance = 0
    start = 0

    for i, ch in enumerate(s):
        if ch == '(':
            balance += 1
        else:  # ')'
            balance -= 1
            if balance < 0:
                raise ValueError("Unbalanced input: ')' encountered before a matching '('.")

        if balance == 0:
            groups.append(s[start:i + 1])
            start = i + 1

    if balance != 0:
        raise ValueError("Unbalanced input: not all '(' are closed by ')'.")
    return groups