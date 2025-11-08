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

# Approach 1: Simple trial division up to sqrt(n), odd-only
def is_prime(n) -> bool:
    n = _coerce_to_int(n)
    if n is None or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    r = int(n**0.5)
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True
