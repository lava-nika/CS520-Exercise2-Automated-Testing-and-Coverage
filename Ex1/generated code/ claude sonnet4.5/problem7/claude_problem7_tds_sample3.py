def count_nums(arr):
    def digit_sum(n):
        if n == 0:
            return 0
        if n > 0:
            return sum(int(d) for d in str(n))
        # For negative: first digit negative, rest positive
        s = str(n)[1:]
        return -int(s[0]) + sum(int(d) for d in s[1:])
    
    return sum(digit_sum(num) > 0 for num in arr)

