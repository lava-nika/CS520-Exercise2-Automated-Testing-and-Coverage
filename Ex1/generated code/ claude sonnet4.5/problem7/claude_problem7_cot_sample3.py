def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, 3.
    
    >>> count_nums([]) == 0
    True
    >>> count_nums([-1, 11, -11]) == 1
    True
    >>> count_nums([1, 1, 2]) == 3
    True
    """
    def digit_sum(n):
        """Calculate sum of digits with special handling for negative numbers."""
        if n == 0:
            return 0
        
        # Extract digits mathematically
        is_negative = n < 0
        n = abs(n)
        
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        # Digits are in reverse order, reverse them
        digits.reverse()
        
        # For negative numbers, make first digit negative
        if is_negative and digits:
            digits[0] = -digits[0]
        
        return sum(digits)
    
    # Count numbers where digit sum > 0
    return sum(1 for num in arr if digit_sum(num) > 0)

