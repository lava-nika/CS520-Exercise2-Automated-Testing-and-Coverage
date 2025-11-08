def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name.
    """
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
    
    filtered = [num for num in arr if 1 <= num <= 9]
    filtered.sort()
    filtered.reverse()
    result = [digit_to_word[num] for num in filtered]
    
    return result

