from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate multiple balanced parenthesis groups from a string (ignoring spaces).

    Parameters
    ----------
    paren_string : str
        A string containing several balanced parenthesis groups separated by spaces.

    Returns
    -------
    List[str]
        A list of balanced groups without spaces.

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
            # Ignore any non-parenthesis non-space characters (forgiving mode).
            # If you prefer strictness, replace with: raise ValueError("Invalid character")
            continue

        current.append(ch)
        balance += 1 if ch == '(' else -1

        if balance < 0:
            raise ValueError("Unbalanced parentheses: too many closing ')'.")

        if balance == 0:
            # Completed one balanced group
            groups.append(''.join(current))
            current.clear()

    if balance != 0:
        raise ValueError("Unbalanced parentheses: too many opening '('.")

    return groups
