def check_grammar(text):
    punctuation = ["!", "?", "."]
    if text == "":
        return True
    if text[0] == text[0].upper() and text[-1] in punctuation:
        return True
    else:
        return False
        