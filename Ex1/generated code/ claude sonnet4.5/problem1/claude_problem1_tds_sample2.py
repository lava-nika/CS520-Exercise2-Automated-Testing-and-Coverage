from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if len(numbers) < 2:
        return False
    
    return any(abs(a - b) < threshold for a, b in combinations(numbers, 2))


