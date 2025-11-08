def count_nums(arr):
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
            return -digits[0] + sum(digits[1:])
        else:
            return sum(digits)
    
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    return count

