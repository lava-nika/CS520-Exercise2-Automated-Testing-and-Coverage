def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
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
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 is prime
    if n == 2:
        return True
    
    # Check for divisors from 2 to sqrt(n)
    # Using i * i <= n instead of i <= sqrt(n) to avoid floating point operations
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

