def generate_integers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    
    lower = max(lower, 0)
    upper = min(upper, 9)
    
    result = []
    for num in range(lower, upper + 1):
        if num % 2 == 0:
            result.append(num)
    
    return result

