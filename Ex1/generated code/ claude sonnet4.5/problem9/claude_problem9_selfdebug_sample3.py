def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name.
    """
    digit_to_word = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    
    return [digit_to_word[num] for num in sorted([n for n in arr if 1 <= n <= 9], reverse=True)]

