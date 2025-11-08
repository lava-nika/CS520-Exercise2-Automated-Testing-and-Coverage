# Bug 1: Off-by-one error in range check
# Instead of 1-9 inclusive, checks 1-8 
# this is a boundary condition bug.

def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    """
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            if 1 <= var <= 8:  # BUG: Should be <= 9
                new_arr.append(dic[var])
        except:
            pass
    return new_arr
