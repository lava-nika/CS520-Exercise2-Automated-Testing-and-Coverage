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
    # Type validation: prime numbers are defined only for integers
    if not isinstance(n, int) or isinstance(n, bool):
        return False
    
    # Numbers less than or equal to 1 are not prime by definition
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd divisors from 3 up to sqrt(n)
    # We need the +1 to include the square root itself in the range
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    # If no divisors found, n is prime
    return True