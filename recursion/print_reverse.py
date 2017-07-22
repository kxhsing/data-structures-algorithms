def print_reverse(phrase):
    if not phrase:
        return

    last_char = phrase[-1]
    print last_char,
    print_reverse(phrase[:-1])