from lib import get_min, get_max, get_sum, get_multiply, read_file, prepare_lines


def run(file_path):
    lines = read_file(file_path)
    numbers = prepare_lines(lines)
    min_num = get_min(numbers)
    max_num = get_max(numbers)
    sum_of_numbers = get_sum(numbers)
    multiply_of_numbers = get_multiply(numbers)

    print(f"Минимальное значение: {min_num}")
    print(f"Максимальное значение: {max_num}")
    print(f"Сумма всех элементов: {sum_of_numbers}")
    print(f"Произведение всех элементов {multiply_of_numbers}")


FILE_PATH = 'data.txt'
run(FILE_PATH)
