from typing import List

def _signed_digit_sum_string(n: int) -> int:
    """Compute signed digit sum by parsing the string representation."""
    s = str(n)
    if s[0] == '-':
        total = 0
        # s[1:] contains only digits for standard int str(); handle first digit as negative.
        for i, ch in enumerate(s[1:]):
            d = ord(ch) - ord('0')
            if i == 0:
                total -= d
            else:
                total += d
        return total
    else:
        return sum(ord(ch) - ord('0') for ch in s)  # n >= 0


def count_nums(arr: List[int]) -> int:
    """Count using string parsing."""
    cnt = 0
    for n in arr:
        if _signed_digit_sum_string(n) > 0:
            cnt += 1
    return cnt