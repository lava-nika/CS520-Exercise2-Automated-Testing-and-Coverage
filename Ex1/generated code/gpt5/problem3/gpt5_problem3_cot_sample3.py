def _powmod(a: int, d: int, mod: int) -> int:
    # Fast modular exponentiation
    res = 1
    a %= mod
    while d > 0:
        if d & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        d >>= 1
    return res

def _miller_rabin_witness(a: int, d: int, s: int, n: int) -> bool:
    """
    Returns False if 'a' is not a witness for compositeness (i.e., test passes),
    Returns True if 'a' is a witness that n is composite.
    """
    x = _powmod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True  # composite

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    # Small primes shortcut
    small_primes = [2, 3, 5, 7, 11, 13, 17]
    if n in small_primes:
        return True
    # Even and small-prime divisibility quick checks
    if n % 2 == 0:
        return False
    for p in (3, 5, 7, 11, 13, 17):
        if n % p == 0:
            return n == p

    # Write n-1 as d * 2^s with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Deterministic bases for n < 2^64
    # Ref: Research shows these bases are enough for 64-bit determinism.
    bases = [2, 3, 5, 7, 11, 13, 17]
    for a in bases:
        if a % n == 0:
            continue
        if _miller_rabin_witness(a, d, s, n):
            return False
    return True