from cloudinary import models as cloudinary_models
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    image = cloudinary_models.CloudinaryField("image",
                                              null=True,
                                              blank=True,
                                              )
