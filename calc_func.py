from string import punctuation, ascii_letters, digits


def calculate_lines(data: str) -> int:
    number_lines = 0
    for i in data:
        if i == '\n' and i != '\n\n':
            number_lines += 1
    return number_lines


def calculate_words(data: str) -> int:
    in_word = False
    number_words = 0
    for char in data:
        if char != ' ' and char != '\n' and in_word is False and char not in punctuation:
            if ((('а' <= char <= 'я' or 'А' <= char <= 'Я') or ('a' <= char <= 'z' or 'A' <= char <= 'Z'))
                    and char not in digits):
                in_word = True
                number_words += 1
        elif char == ' ' or char == '\n' or char in punctuation:
            in_word = False
    return number_words
