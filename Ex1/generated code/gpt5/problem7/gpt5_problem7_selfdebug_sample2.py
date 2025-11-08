from typing import List

def _signed_digit_sum_numeric(n: int) -> int:
    """Compute signed digit sum without using strings."""
    if n == 0:
        return 0

    x = abs(n)

    # Sum of all digits
    sum_abs = 0
    t = x
    while t > 0:
        sum_abs += t % 10
        t //= 10

    # Most significant digit
    first = x
    while first >= 10:
        first //= 10

    if n >= 0:
        return sum_abs
    else:
        # (-first) + (sum_abs - first) == sum_abs - 2*first
        return sum_abs - 2 * first


def count_nums(arr: List[int]) -> int:
    """Count using numeric digit extraction."""
    cnt = 0
    for n in arr:
        if _signed_digit_sum_numeric(n) > 0:
            cnt += 1
    return cnt
