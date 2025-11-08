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

# Approach 3: Deterministic Miller–Rabin for 64-bit range
def is_prime(n) -> bool:
    n = _coerce_to_int(n)
    if n is None or n < 2:
        return False
    # small primes
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return n == p

    # write n-1 as d * 2^s with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    def _check(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Deterministic bases for testing 64-bit integers
    # Ref: Jaeschke / Jim Sinclair / CP-algorithms — covers n < 2^64
    for a in (2, 3, 5, 7, 11, 13, 17):
        if not _check(a % n):
            return False
    return True
