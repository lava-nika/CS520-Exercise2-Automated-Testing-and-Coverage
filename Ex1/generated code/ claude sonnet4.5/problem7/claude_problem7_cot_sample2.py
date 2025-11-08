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
        
        if n > 0:
            # For positive numbers, sum all digits
            return sum(int(digit) for digit in str(n))
        
        # For negative numbers: first digit is negative, rest are positive
        # Convert to string, remove '-' sign, get digits
        digits_str = str(abs(n))
        
        # First digit is negative
        first_digit = -int(digits_str[0])
        
        # Rest of digits are positive
        rest_sum = sum(int(digit) for digit in digits_str[1:])
        
        return first_digit + rest_sum
    
    # Count numbers where digit sum > 0
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    
    return count

