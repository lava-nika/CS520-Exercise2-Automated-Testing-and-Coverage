from solution import make_palindrome


def test_empty_string():
    """Covers the explicit 'if not string: return '' ' branch."""
    assert make_palindrome('') == ''


def test_already_palindrome_zero_iterations():
    """Covers the case where the while loop condition is immediately false (0 iterations)."""
    # 'racecar' is already a palindrome. beginning_of_suffix remains 0.
    assert make_palindrome('racecar') == 'racecar'
    assert make_palindrome('aba') == 'aba'
    

def test_single_character_zero_iterations():
    """Covers the minimal, already-palindrome case (single character)."""
    # 'a' is a palindrome. beginning_of_suffix remains 0.
    assert make_palindrome('a') == 'a'


def test_one_iteration_required():
    """Covers the case where the while loop runs exactly once."""
    # 'ab' -> 'b' is not palindrome. beginning_of_suffix=1. Loop stops. Returns 'ab' + 'a'.
    assert make_palindrome('ab') == 'aba'
    # 'abaa' -> 'baa' not, 'aa' is. beginning_of_suffix=2. Loop runs twice. Returns 'abaa' + 'ba'.
    assert make_palindrome('abaa') == 'abaaba'
    

def test_multiple_iterations_no_suffix():
    """Covers the maximum iteration path (n-1 iterations) where the only palindromic suffix is the last character."""
    # 'abc'. Suffixes: 'abc' (no), 'bc' (no), 'c' (yes). beginning_of_suffix = 2.
    # Appends 'ba' to 'abc' -> 'abcba'.
    assert make_palindrome('abc') == 'abcba'
    

def test_partial_palindromic_suffix():
    """Covers a multi-character string requiring multiple iterations to find the longest palindromic suffix."""
    # 'abac'
    # 'abac' (no), 'bac' (no), 'ac' (no), 'c' (yes). beginning_of_suffix = 3.
    # Appends 'aba' to 'abac' -> 'abacaba'.
    assert make_palindrome('abac') == 'abacaba'
    

def test_long_string_with_internal_palindrome():
    """Covers a longer, more complex string to ensure the loop and suffix logic is robust."""
    # 'google'
    # Suffixes: 'google', 'oogle', 'ogle', 'gle', 'le', 'e' (yes). beginning_of_suffix = 5.
    # Appends 'lgoog' to 'google' -> 'googlelgoog'.
    assert make_palindrome('google') == 'googlelgoog'
    # 'xabacb' -> Suffixes: 'xabacb', 'abacb', 'bacb', 'acb', 'cb', 'b' (Yes). beginning_of_suffix=5.
    # Returns 'xabacb' + ('xabac')[::-1] = 'xabacb' + 'cabax' -> 'xabacbcabax'
    assert make_palindrome('xabacb') == 'xabacbcabax'
