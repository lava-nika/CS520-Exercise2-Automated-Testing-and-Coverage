def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    """
    # Mapping from digit to word
    digit_to_word = {
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
    
    # Step 1: Filter - keep only numbers between 1 and 9 inclusive
    filtered = [num for num in arr if isinstance(num, int) and 1 <= num <= 9]
    
    # Step 2: Sort in ascending order
    filtered.sort()
    
    # Step 3: Reverse to get descending order
    filtered.reverse()
    
    # Step 4: Convert digits to words
    result = [digit_to_word[num] for num in filtered]
    
    return result

