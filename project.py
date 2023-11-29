from string import punctuation

def open_file(file_name):
    with (open(file_name) as file):
        data = file.read()
        return data


def calculate_lines(data: str) -> int:
    number_lines = 0
    for i in data:
        print(i)
        if i == ('\n'):
            number_lines += 1
            print(number_lines)
    return number_lines


def calculate_words(data: str) -> int:
    in_word = False
    number_words = 0
    for i in data:
        if i != ' ' and i != '\n' and in_word == False:
            number_words += 1
            in_word = True
        elif i == ' ' or i == '\n':
            in_word == False
            print(number_words)
    return number_words


f = input('Введите путь до файла: ')
text = open_file(f)
print(text)
print("Количество строк:", calculate_lines(text))
print("Количество слов:", calculate_words(text))


