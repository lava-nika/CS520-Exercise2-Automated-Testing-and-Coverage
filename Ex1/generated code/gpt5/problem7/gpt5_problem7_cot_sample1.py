from typing import List

def count_nums(arr: List[int]) -> int:
    """
    Return the count of numbers whose signed-digit sum > 0.
    For negatives, only the most significant digit is negated.

    Examples
    --------
    >>> count_nums([]) == 0
    True
    >>> count_nums([-1, 11, -11]) == 1
    True
    >>> count_nums([1, 1, 2]) == 3
    True
    """
    def signed_digit_sum(n: int) -> int:
        s = str(abs(n))
        sum_abs = sum(int(ch) for ch in s)  # sum of absolute digits
        if n >= 0:
            return sum_abs
        first_digit = int(s[0])
        # For negative numbers, first digit is negated instead of positive:
        # (-first_digit + rest) = (first_digit + rest) - 2*first_digit = sum_abs - 2*first_digit
        return sum_abs - 2 * first_digit

    return sum(1 for x in arr if signed_digit_sum(x) > 0)
