def sum_two(x, y):
    return x + y


def sum_list(numbers):
    result = 0

    for number in numbers:
        result = sum_two(result, number)

    return result


result = sum_list([1, 2])
print(result == 3)


def validate_positive(value):
    if value <= 0:
        raise ValueError("Value must be positive")
    return value
