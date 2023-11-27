def open_file(file_name):
    with (open(file_name) as file):
        data = file.read()
        file.seek(0)
        lines = file.readlines()
        return data, lines


def calculate_lines(lines: list) -> int:
    return len(lines)


def calculate_words(data: str) -> int:
    for i in data:
        print(i)


open_file('text.txt')
calculate_words(data)
# разобраться как работает возврат внутри функции и как использовать данные в других
