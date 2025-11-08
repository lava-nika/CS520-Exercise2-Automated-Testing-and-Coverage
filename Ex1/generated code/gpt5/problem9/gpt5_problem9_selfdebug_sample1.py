from typing import Iterable, List

def by_length(arr: Iterable[int]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array (i.e., sort descending), and then replace each digit
    by its corresponding name: "One".."Nine".

    Examples
    --------
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    >>> by_length([])
    []
    >>> by_length([1, -1, 55])
    ['One']
    """
    names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    # Filter: keep only true ints in [1, 9]; exclude bools which are subclasses of int
    digits = [x for x in arr if isinstance(x, int) and not isinstance(x, bool) and 1 <= x <= 9]

    # Sort descending
    digits.sort(reverse=True)

    # Map to names
    return [names[d] for d in digits]
