from distutils.command.build_scripts import first_line_re

from letter_count import letter_count
from palindrome import palindrome
from panagram import panagram
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


def test_panagram():
    assert panagram('abcdefghijklmnopqrstuvwxyz') == True
    assert panagram('my name is ') == False


def test_letter_count():
    assert letter_count("navas shareef") == {
        'n': 1, 'a': 3, 'v': 1, 's': 2, 'h': 1, 'r': 1, 'e': 2, 'f': 1}
    assert letter_count("navas") != {
        'n': 1, 'a': 3, 'v': 1, 's': 2, 'h': 1, 'r': 1, 'e': 2, 'f': 1}
