def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name.
    
    FIXES:
    - Added type checking to ensure only integers are processed
    - Handles floats and non-numeric types gracefully
    """
    # Mapping of digits to names
    digit_to_name = {
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
    
    # Filter: only integers between 1 and 9 inclusive
    # isinstance(num, int) checks for int type
    # 'not isinstance(num, bool)' excludes booleans (bool is subclass of int in Python)
    filtered = [num for num in arr 
                if isinstance(num, int) and not isinstance(num, bool) 
                and 1 <= num <= 9]
    
    # Sort in ascending order
    filtered.sort()
    
    # Reverse to get descending order
    filtered.reverse()
    
    # Map to names
    result = [digit_to_name[num] for num in filtered]
    
    return result