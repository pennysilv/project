def open_file(file_name):
    with (open(file_name) as file):
        data = file.read()
        file.seek(0)
        lines = file.readlines()
        return data, lines


def calculate_lines(lines: list) -> int:
    number_lines = len(lines)
    return number_lines


def calculate_words(data: str) -> int:
    number_words = 0
    words = data.split()
    for i in range(len(words)):
        number_words += 1
    return number_words

f = input('Введите путь до файла: ')
text, list_of_strings = open_file(f)
print(text)
print("Количество строк:", calculate_lines(list_of_strings))
print("Количество слов:", calculate_words(text))


