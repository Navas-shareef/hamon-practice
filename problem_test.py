from palindrome import palindrome
from primality import prime


def test_palindrome_with_non_palindrome_words():
    assert palindrome('english') == False
    assert palindrome('ball') == False


def test_palindrome_with_palindrome_words():
    assert palindrome('malayalam') == True


def test_with_non_prime_number():
    assert prime(4) == False


def test_with_prime_number():
    assert prime(3) == True
