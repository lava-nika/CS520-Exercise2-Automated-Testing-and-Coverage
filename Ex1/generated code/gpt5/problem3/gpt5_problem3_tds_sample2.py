from typing import Optional

def _coerce_to_int(n: Optional[object]) -> Optional[int]:
    """Return an int if n is an integer-valued number; otherwise None."""
    if n is None:
        return None
    # Fast path for int
    if isinstance(n, bool):
        # Treat booleans as non-prime (avoid True==1 confusion)
        return None
    if isinstance(n, int):
        return n
    # Allow integer-valued floats
    if isinstance(n, float):
        if n.is_integer():
            return int(n)
        return None
    # Reject other types (str, list, etc.)
    return None

# Approach 2: 6k±1 wheel optimization trial division
def is_prime(n) -> bool:
    n = _coerce_to_int(n)
    if n is None or n < 2:
        return False
    # small quick checks
    for p in (2, 3, 5):
        if n == p:
            return True
        if n % p == 0:
            return n == p
    # numbers of form 6k ± 1 can be prime
    i = 6
    limit = int(n**0.5)
    while i - 1 <= limit:
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0 and i + 1 <= limit:
            return False
        i += 6
    return True