def is_prime(n: int) -> bool:
    """Return True if a given number is prime, and False otherwise.

    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        return False
    if n <= 3:
        # 2 and 3 are prime
        return True
    # Eliminate multiples of 2 or 3 early
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check factors of the form 6k ± 1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
