def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digit_sum(num):
        """Calculate the sum of digits with special handling for negatives"""
        if num == 0:
            return 0
        
        # Work with absolute value to extract digits
        abs_num = abs(num)
        digits = [int(d) for d in str(abs_num)]
        
        # If original number was negative, make first digit negative
        if num < 0:
            digits[0] = -digits[0]
        
        return sum(digits)
    
    # Count numbers with digit sum > 0
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    
    return count