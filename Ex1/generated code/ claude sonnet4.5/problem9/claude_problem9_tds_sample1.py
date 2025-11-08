def by_length(arr):
    digit_to_name = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    
    valid_nums = [num for num in arr if 1 <= num <= 9]
    valid_nums.sort()
    valid_nums.reverse()
    
    return [digit_to_name[num] for num in valid_nums]

