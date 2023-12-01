from string import punctuation, ascii_letters, digits


def open_file(file_name, encoding='utf-8'):
    with (open(file_name) as file):
        data = file.read()
        return data


def calculate_lines(data: str) -> int:
    number_lines = 0
    for i in data:
        if i == '\n' and i != '\n\n':
            number_lines += 1
    return number_lines


def calculate_words(data: str) -> int:
    in_word = False
    number_words = 0
    kirill = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin = ascii_letters
    words = []
    for i in data:
        if i != ' ' and i != '\n' and in_word is False and i not in punctuation:
            if (i in kirill or latin) and i not in digits:
                in_word = True
                number_words += 1
        elif i == ' ' or i == '\n' or i in punctuation:
            in_word = False
    return number_words


f = input('Введите путь до файла: ')
text = open_file(f)
print(text)
print("Количество строк:", calculate_lines(text))
print("Количество слов:", calculate_words(text))


