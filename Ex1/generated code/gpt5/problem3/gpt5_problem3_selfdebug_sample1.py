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
    # Validate input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    # 0, 1, and negatives are not prime
    if n <= 1:
        return False

    # 2 and 3 are primes
    if n <= 3:
        return True

    # Exclude even numbers
    if n % 2 == 0:
        return False

    # Check only odd divisors up to √n
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True
