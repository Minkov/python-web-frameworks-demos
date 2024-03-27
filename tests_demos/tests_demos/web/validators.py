from django.core import exceptions


def validate_book_title(value):
    if not value[0].isupper():
        raise exceptions.ValidationError("Book title must start with an uppercase letter")
