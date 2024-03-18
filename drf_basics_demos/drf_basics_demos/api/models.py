from django.db import models


class Genre(models.TextChoices):
    Fantasy = "Fantasy"
    ScienceFiction = "Science-Fiction"


class Author(models.Model):
    name = models.CharField(max_length=24)


class Book(models.Model):
    title = models.CharField(max_length=20)

    pages = models.IntegerField(default=0)

    description = models.TextField(max_length=100, default="")

    genre = models.CharField(
        max_length=max(len(choice) for choice, _ in Genre.choices),
        choices=Genre.choices,
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
