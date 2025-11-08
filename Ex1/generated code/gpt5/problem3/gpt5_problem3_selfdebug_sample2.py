def is_prime(n) -> bool:
    # Type guard: only integers are considered
    if not isinstance(n, int):
        return False
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True