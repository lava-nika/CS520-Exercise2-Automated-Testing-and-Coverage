from typing import List, Iterable

def by_length(arr: Iterable[int]) -> List[str]:
    """
    Given an array of integers, keep only those in [1, 9], sort them ascending,
    reverse to descending, and map to their English names.

    Examples
    --------
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    >>> by_length([])
    []
    >>> by_length([1, -1, 55])
    ['One']
    """
    # Mapping index by digit; index 0 is a placeholder to make indices align with digits
    names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    # 1) Filter to valid digits (robust to non-ints)
    digits = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]

    # 2) Sort ascending then reverse (or just sort with reverse=True)
    digits.sort(reverse=True)

    # 3) Map digits to names
    return [names[d] for d in digits]
