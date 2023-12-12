from string import punctuation, ascii_letters, digits


def calculate_lines(data: str) -> int:
    line_count = 0
    empty_line = True
    for ch in data:
        if ch == '\n' and empty_line:
            pass
        elif ch == '\n' and not empty_line:
            empty_line = True
            line_count += 1
        else:
            empty_line = False
    if not empty_line:
        line_count += 1
    return line_count


def is_symbol(ch: str) -> bool:
    return  'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or 'А' <= ch <= 'Я' or 'а' <= ch <= 'я'


def calculate_words(data: str) -> int:
    in_word = False
    number_words = 0
    for char in data:
        if char != ' ' and char != '\n' and in_word is False and char not in punctuation:
            if is_symbol(char) and char not in digits:
                in_word = True
                number_words += 1
        elif char == ' ' or char == '\n' or char in punctuation:
            in_word = False
    return number_words


def calculate_symbols(data: str) -> int:
    count_symbols = 0
    for ch in data:
        if is_symbol(ch):
            count_symbols += 1
    return count_symbols


def is_link(data: str) -> bool:
    i = 0
    if i == len(data) or data[i] != '[':
        return False
    i += 1
    while i < len(data) and is_symbol(data[i]):
        i += 1
    if i == len(data) or data[i] != ']':
        return False
    i += 1
    return True

# def calculate_link(data: str) -> int:
#     i = 0
#     if data[i] != '[':
#         return


# def calculate_emails(data: str) -> int:
#     count = 0
#     has_symbol = True
#     has_dog = False
#     while ch < len(data):
#         while not has_dog and ch in ascii_letters:
#             ch += 1
#             has_symbol = True
#         if ch == '@':
#             has_dog = True
#         while ch < len(data) and ch in ascii_letters:
#
#
# def is_symbol(ch: str) -> bool:
#     return  'a' <= ch <= 'z' or '0' <= ch <= '9'
#
#
# def read_word(data: str) -> (bool, str):
#     i = 0
#     while i < len(data) and is_symbol(data[i]):
#         i += 1
#     if i == 0:
#         return False, ""
#     return True, data[i:]
#
# def read_dog(data: str) -> (bool, str):
#     if len(data) == 0 or data[0] != '@':
#         return False, ""
#     return True, data[1:]
# def is_email(data: str):
#     i = 0
#     while i < len(data) and is_symbol(data[i]):
#         i += 1
#     if i == 0:
#         return False
#
#     if len(data) == 0 or data[0] != '@':
#         return False
#     i += 1
#
#     i = 0
#     while i < len(data) and is_symbol(data[i]):
#         i += 1
#     if i == 0:
#         return False
#
# def is_email(data: str) -> (bool, str):
#     ok, data = read_word(data)
#     if not ok:
#         return False
#     ok, data = read_dog(data)
#     if not ok:
#         return False
#     ok, data = read_word(data)
#     if not ok:
#         return False
#     return True