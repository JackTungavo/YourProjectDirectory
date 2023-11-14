from lib.make_snippet import *

# Test less than 5 words
# Test more than 5 words
# Test equal to 5 words

def test_make_snippet_empty_string():
    assert make_snippet("") == ""

def test_make_snippet_less_than_5_words():
    assert make_snippet("How are you today?") == "How are you today?"

def test_make_snippet_greater_than_5_words():
    assert make_snippet("Hello, how are you today, are you ok?") == "Hello, how are you today,..."

def test_make_snippet_equal_to_5_words():
    assert make_snippet("Hello, how are you today?") == "Hello, how are you today?"