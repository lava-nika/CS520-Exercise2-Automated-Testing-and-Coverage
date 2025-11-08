def _powmod(a: int, d: int, mod: int) -> int:
    # Fast modular exponentiation (binary exponentiation)
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
    Return True if 'a' is a witness that n is composite; False otherwise.
    """
    x = _powmod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True

def is_prime(n) -> bool:
    # Type guard
    if not isinstance(n, int):
        return False
    # Base cases
    if n <= 1:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17)
    if n in small_primes:
        return True
    if n % 2 == 0:
        return False
    # Quick trial division by small primes
    for p in (3, 5, 7, 11, 13, 17):
        if n % p == 0:
            return n == p

    # Write n - 1 = d * 2^s with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Deterministic bases for 64-bit integers
    for a in small_primes:
        if a % n == 0:
            continue
        if _miller_rabin_witness(a, d, s, n):
            return False
    return True