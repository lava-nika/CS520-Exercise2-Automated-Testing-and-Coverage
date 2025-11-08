from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate multiple balanced parenthesis groups from a string (ignoring spaces).

    Returns a list where each element is one balanced group with spaces removed.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    >>> separate_paren_groups('() (()) (()())')
    ['()', '(())', '(()())']
    >>> separate_paren_groups('   ')
    []
    """
    groups: List[str] = []
    current: List[str] = []
    balance = 0

    for ch in paren_string:
        if ch == ' ':
            continue
        if ch not in ('(', ')'):
            # Forgiving mode: ignore non-parenthesis, non-space chars.
            # To be strict, replace with: raise ValueError("Invalid character in input.")
            continue

        # Update state
        current.append(ch)
        balance += 1 if ch == '(' else -1

        # Defensive checks for unbalanced input
        if balance < 0:
            raise ValueError("Unbalanced parentheses: extra ')' encountered.")

        # Completed a balanced group
        if balance == 0:
            groups.append(''.join(current))
            current.clear()

    # If balance is not zero, we have leftover '('
    if balance != 0:
        raise ValueError("Unbalanced parentheses: extra '(' remaining.")

    return groups
