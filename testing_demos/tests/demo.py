from django.core.exceptions import ValidationError


def add_1(x):
    return sum(x, 1)


def add_1_to_each_in_list(ll):
    return [add_1(x) for x in ll]


def test_with_empty_list():
    ll = []
    result = add_1_to_each_in_list(ll)
    if ll != result:
        raise Exception('List must be empty')


def non_empty_string_validator(value):
    if value is None or value == '':
        raise ValidationError
