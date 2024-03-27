# Not this:
# from unittest import TestCase
# This:
from django.core import exceptions
from django.test import TestCase

from tests_demos.web.models import Author, Book


class TestBook(TestCase):
    def test_book_create__when_title_starts_with_uppercase__expect_to_be_created(self):
        # Arrange
        title = "The book"
        author = Author.objects.create(name="The author")

        # Act
        book = Book.objects.create(title=title, author=author)
        book.full_clean()

        # Assert
        self.assertIsNotNone(book)

    def test_book_create__when_title_starts_lowercase__expect_validation_error(self):
        # Arrange
        title = "the book"
        author = Author.objects.create(name="The author")

        # Act
        with self.assertRaises(exceptions.ValidationError) as context:
            book = Book.objects.create(title=title, author=author)
            book.full_clean()

        exception = context.exception
        title_exception = str(exception.error_dict["title"][0])

        self.assertEqual("['Book title must start with an uppercase letter']", title_exception)
