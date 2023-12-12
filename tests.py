from calc_func import *

if __name__ == '__main__':
    assert calculate_lines("") == 0
    assert calculate_lines("\n") == 0
    assert calculate_lines("a\nb\nc") == 3
    assert calculate_lines("a\nb\n\n") == 2

    assert calculate_words("a b c") == 3
    assert calculate_words("fff aaa ccc") == 3
    assert calculate_words("444 aaa.") == 1
    assert calculate_words("арара ляля") == 2

    assert calculate_symbols('abc') == 3
    assert calculate_symbols('a b c') == 3
    assert calculate_symbols('a.b.c') == 3
    assert calculate_symbols('a\nb\nc') == 3

    assert is_link('[]') == True
    assert is_link('[aaa]') == True
    assert is_link(']') == False
    assert is_link('[') == False
    assert is_link('][') == False
    assert is_link('[lalala]') == True

    # assert(calculate_emails("") == 0)
    # assert(calculate_emails("ilya@lispberry.dev") == 1)
    # assert(calculate_emails("ilya@@lispberry.dev") == 0)
    # assert(calculate_emails("@@@") == 1)
    # assert(calculate_emails(" @ ") == 0)
    # assert(calculate_emails(" @") == 0)
    # assert(calculate_emails(",@@") == 1)
    # assert (calculate_emails(",@,") == 1)




