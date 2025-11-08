def by_length(arr):
    names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    valid_nums = [num for num in arr if 1 <= num <= 9]
    valid_nums.sort(reverse=True)
    
    return [names[num] for num in valid_nums]

