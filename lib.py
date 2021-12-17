def read_file(file_path):
    f = open(file_path)
    lines = f.readlines()
    f.close()
    return lines


def prepare_lines(lines):
    numbers = []
    for line in lines:
        line.replace('\n', '')
        chars = line.split(' ')
        for char in chars:
            try:
                num = int(char)
                numbers.append(num)
            except ValueError:
                print("Wrong value")

    return numbers


def get_min(numbers):
    if len(numbers) == 0:
        return

    min_val = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]

    return min_val


def get_max(numbers):
    if len(numbers) == 0:
        return

    max_val = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]

    return max_val


def get_sum(numbers):
    if len(numbers) == 0:
        return 0

    res = 0
    for num in numbers:
        res += num

    return res


def get_multiply(numbers):
    if len(numbers) == 0:
        return 0

    res = 1

    try:
        for num in numbers:
            res *= num
    except ArithmeticError:
        res = 0

    return res