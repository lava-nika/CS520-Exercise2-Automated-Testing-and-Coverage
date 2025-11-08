def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, 3.
    """
    def digit_sum(n):
        if n == 0:
            return 0
        
        is_negative = n < 0
        n = abs(n)
        
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.reverse()
        
        if is_negative:
            digits[0] = -digits[0]
        
        return sum(digits)
    
    return sum(1 for num in arr if digit_sum(num) > 0)

