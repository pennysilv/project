from calc_func import calculate_lines, calculate_words


def read_whole_file(file_name, encoding='utf-8'):
    with (open(file_name) as file):
        data = file.read()
        return data


f = input('Введите путь до файла: ')
text = read_whole_file(f)
print(text)
print("Количество строк:", calculate_lines(text))
print("Количество слов:", calculate_words(text))


