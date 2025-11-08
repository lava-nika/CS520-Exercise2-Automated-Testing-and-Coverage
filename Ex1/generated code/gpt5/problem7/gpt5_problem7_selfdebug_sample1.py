from typing import Iterable

def count_nums(arr: Iterable[int]) -> int:
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, 3.

    >>> count_nums([]) == 0
    True
    >>> count_nums([-1, 11, -11]) == 1
    True
    >>> count_nums([1, 1, 2]) == 3
    True
    """
    def signed_digit_sum(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("count_nums expects an iterable of integers")
        s = str(abs(n))
        total = sum(int(ch) for ch in s)  # sum of absolute digits
        if n >= 0:
            return total
        first = int(s[0])                 # most significant digit
        return total - 2 * first          # negate the first digit

    return sum(1 for x in arr if signed_digit_sum(x) > 0)
