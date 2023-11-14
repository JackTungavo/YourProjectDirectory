from lib.check_grammar import *

def test_check_grammar_empty_string():
    assert check_grammar("") == True

def test_check_grammar_no_capital_but_exclamation():
    assert check_grammar("hello!") == False

def test_check_grammar_no_capital_but_full_stop():
    assert check_grammar("hello.") == False

def test_check_grammar_no_capital_but_question_mark():
    assert check_grammar("hello?") == False

def test_check_grammar_capital_but_no_punctuation():
    assert check_grammar("Hello") == False

def test_check_grammar_no_capital_no_punctuation():
    assert check_grammar("hello") == False

def test_check_grammar_incorrect_punctuation():
    assert check_grammar("Hello,") == False

def test_check_grammar_capital_and_correct_punctuation():
    assert check_grammar("Hello!") == True