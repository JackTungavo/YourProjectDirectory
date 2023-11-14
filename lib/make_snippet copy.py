def make_snippet(string):
    words = string.split()
    string_to_return = ""
    if len(words) > 5:
        for i in range(0,5):
            if i == 4:
                string_to_return += words[i]
            else:
                string_to_return += (words[i] + " ")
        string_to_return += "..."
    else:
        return string
    return string_to_return