def generate_integers(a, b):
    lower = max(min(a, b), 0)
    upper = min(max(a, b), 9)
    
    if lower > upper:
        return []
    
    return list(filter(lambda x: x % 2 == 0, range(lower, upper + 1)))

