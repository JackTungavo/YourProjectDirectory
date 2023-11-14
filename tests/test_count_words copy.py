from lib.count_words import *

# Given an empty string - return 0

def test_count_words_empty_string_return_0():
    assert count_words("") == 0

# Given a string - return number of words in string

def test_count_words_sentence_string():
    assert count_words("Hello how are you?") == 4