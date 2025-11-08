from solution import by_length


def test_empty_array():
    """Covers the minimal case: an empty input array."""
    assert by_length([]) == []


def test_valid_range_and_sorting_verification():
    """Covers valid numbers (1-9) and verifies descending sorting order."""
    # Input: [2, 1, 5, 3]. Sorted: [5, 3, 2, 1]. Output: ["Five", "Three", "Two", "One"]
    assert by_length([2, 1, 5, 3]) == ["Five", "Three", "Two", "One"]


def test_valid_range_with_duplicates():
    """Covers valid numbers with duplicates, ensuring all are included and sorting is stable/correct."""
    # Input: [9, 9, 1, 1]. Sorted: [9, 9, 1, 1]. Output: ["Nine", "Nine", "One", "One"]
    assert by_length([9, 9, 1, 1]) == ["Nine", "Nine", "One", "One"]


def test_out_of_range_positives_only():
    """Crucial test: Triggers the `except` path for values > 9 (e.g., 10+)."""
    # Input: [10, 500, 100]. All are > 9, all trigger KeyError and are filtered out.
    assert by_length([10, 500, 100]) == []


def test_out_of_range_negatives_and_zero():
    """Crucial test: Triggers the `except` path for 0 and negative numbers."""
    # Input: [0, -1, -50]. All trigger KeyError and are filtered out.
    assert by_length([0, -1, -50]) == []


def test_mixed_valid_and_invalid_numbers():
    """Covers mixed input to ensure both `try` and `except` branches are hit within one run, and sorting is correct."""
    # Input: [2, 10, 1, 14, 9, 0, 4]
    # Valid and sorted: [9, 4, 2, 1] (from the original input)
    # Invalid: [14, 10, 0] (filtered out by exception)
    # Output: ["Nine", "Four", "Two", "One"]
    assert by_length([2, 10, 1, 14, 9, 0, 4]) == ["Nine", "Four", "Two", "One"]


def test_maximum_range_edge_cases():
    """Tests the boundary values of 1 and 9 to ensure dictionary boundaries are correct."""
    # Input: [9, 1, 5, 9, 1]. Sorted: [9, 9, 5, 1, 1].
    assert by_length([9, 1, 5, 9, 1]) == ["Nine", "Nine", "Five", "One", "One"]
