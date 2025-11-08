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
    
    # Filter valid numbers (1-9), sort in reverse (descending), and map to words
    return [
        digit_to_word[num] 
        for num in sorted([n for n in arr if isinstance(n, int) and 1 <= n <= 9], reverse=True)
    ]

