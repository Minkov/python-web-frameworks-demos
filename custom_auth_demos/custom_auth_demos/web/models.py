from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from custom_auth_demos.accounts.models import Profile

UserModel = get_user_model()


# No table needed
class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Model1(AuditModel, models.Model):
    field = models.CharField(max_length=20)

    # Do this
    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.DO_NOTHING,
    # )
    # Example: request.user.model1_set()

    # DO NOT do this:
    # profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.DO_NOTHING,
    # )
    # Example: request.user.profile.model1_set()

#
# @receiver(post_save, sender=Model1)
# def model1_created(sender, instance, created, *args, **kwargs):
#     print([sender, instance, created, args, kwargs])
