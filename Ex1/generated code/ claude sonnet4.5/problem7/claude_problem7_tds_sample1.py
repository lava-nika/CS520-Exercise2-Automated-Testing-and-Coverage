def count_nums(arr):
    def digit_sum(n):
        if n == 0:
            return 0
        
        if n < 0:
            digits_str = str(n)[1:]
            total = -int(digits_str[0])
            for digit in digits_str[1:]:
                total += int(digit)
            return total
        else:
            return sum(int(digit) for digit in str(n))
    
    return sum(1 for num in arr if digit_sum(num) > 0)

