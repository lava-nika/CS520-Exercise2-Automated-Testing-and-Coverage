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
        
        if n > 0:
            return sum(int(digit) for digit in str(n))
        
        # For negative numbers
        digits_str = str(abs(n))
        first_digit = -int(digits_str[0])
        rest_sum = sum(int(digit) for digit in digits_str[1:])
        
        return first_digit + rest_sum
    
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    
    return count

