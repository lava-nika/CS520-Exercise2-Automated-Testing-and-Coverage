from typing import List
import math

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Solution A: Streaming builder with a balance counter.
    Ignores spaces, validates parentheses.
    """
    groups: List[str] = []
    current: List[str] = []
    balance = 0

    for ch in paren_string:
        if ch == ' ':
            continue
        if ch not in ('(', ')'):
            raise ValueError(f"Unexpected character {ch!r}. Only '(' , ')' and spaces are allowed.")

        if ch == '(':
            balance += 1
            current.append(ch)
        else:  # ch == ')'
            balance -= 1
            if balance < 0:
                raise ValueError("Unbalanced input: ')' encountered before a matching '('.")
            current.append(ch)

        if balance == 0 and current:
            groups.append(''.join(current))
            current.clear()

    if balance != 0:
        raise ValueError("Unbalanced input: not all '(' are closed by ')'.")
    return groups