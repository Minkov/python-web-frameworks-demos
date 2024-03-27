from django.db import models

from tests_demos.web.validators import validate_book_title


class Author(models.Model):
    MAX_NAME_LENGTH = 100
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )


class Genre(models.TextChoices):
    FANTASY = "fantasy", "Fantasy"
    HORROR = "horror", "Horror"
    SCIENCE_FICTION = "science_fiction", "Science Fiction"
    ACTION = "action", "Action"
    COMEDY = "comedy", "Comedy"
    ROMANCE = "romance", "Romance"
    ADVENTURE = "adventure", "Adventure"
    THRILLER = "thriller", "Thriller"


class Book(models.Model):
    MAX_TITLE_LENGTH = 100
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
        # Test it
        validators=(
            validate_book_title,
        ),
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    genre = models.CharField(
        max_length=max(len(x) for _, x in Genre.choices),
        choices=Genre.choices,
        default=Genre.FANTASY,
    )

    # Test it
    def __str__(self):
        return f'{self.title} by {self.author.name}'
