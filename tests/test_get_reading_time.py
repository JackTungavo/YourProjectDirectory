from lib.get_reading_time import *

def test_get_reading_time_when_text_length_zero():
    assert get_reading_time("",200) == 0

def test_get_reading_time_for_5_word_text():
    assert get_reading_time("one two three four five", 200) == 5/200

def test_get_reading_time_for_5_words_100_speed():
    assert get_reading_time("one two three four five", 100) == 5/100

long_text = """
In the last exercise, you were given a design for a function, wrote some tests, and then implemented the behaviour to make those tests pass.
However, in industry an engineer will rarely be given a design. They will instead be given a problem to solve. They will then have to decide how to design their program to solve the problem.
To support you in growing towards this, we will use the idea of Design Recipes. You might use different design recipes for different kinds of program. We will start off with a simple one for a single-function program.
Here is a template for you to use. Steps 1 and 2 are new, and steps 3 and 4 are what you did in the last exercise.
"""

def test_get_reading_time_for_long_text():
    assert get_reading_time(long_text, 200) == 125/200