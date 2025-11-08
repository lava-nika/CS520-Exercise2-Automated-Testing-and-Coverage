def generate_integers(a, b):
    lower = max(min(a, b), 0)
    upper = min(max(a, b), 9)
    
    return [num for num in range(lower, upper + 1) if num % 2 == 0]

