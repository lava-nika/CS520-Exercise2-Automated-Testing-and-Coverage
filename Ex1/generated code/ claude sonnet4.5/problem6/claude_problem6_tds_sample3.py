def correct_bracketing(brackets: str):
    balance = 0
    
    for char in brackets:
        balance += 1 if char == '(' else -1
        if balance < 0:
            return False
    
    return balance == 0

