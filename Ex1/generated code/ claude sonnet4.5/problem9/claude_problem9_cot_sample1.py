def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    """
    # Dictionary mapping digits to their English names
    digit_names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    # Step 1: Filter numbers between 1 and 9 inclusive
    filtered = [num for num in arr if 1 <= num <= 9]
    
    # Step 2: Sort the filtered array
    filtered.sort()
    
    # Step 3: Reverse the sorted array
    filtered.reverse()
    
    # Step 4: Convert each digit to its corresponding name
    result = [digit_names[num] for num in filtered]
    
    return result