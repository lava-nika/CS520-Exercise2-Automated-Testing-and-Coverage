from typing import List

def _signed_digit_sum_string(n: int) -> int:
    """Compute the signed digit sum by parsing the string representation."""
    s = str(n)
    if s[0] == '-':
        # Handle negative: first digit after '-' is negative; the rest positive
        # Note: int(-0) becomes '0', so '-' won’t appear for zero.
        total = 0
        for i, ch in enumerate(s[1:]):
            d = ord(ch) - ord('0')
            if i == 0:
                total += -d
            else:
                total += d
        return total
    else:
        # Non-negative: all digits positive
        return sum(ord(ch) - ord('0') for ch in s)

def count_nums(arr: List[int]) -> int:
    """Count numbers with signed digit sum > 0 using string parsing."""
    cnt = 0
    for n in arr:
        if _signed_digit_sum_string(n) > 0:
            cnt += 1
    return cnt