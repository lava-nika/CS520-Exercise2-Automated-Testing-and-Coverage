from typing import List

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        # 2 and 3 are prime
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    # Using i*i <= n avoids computing sqrt
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True