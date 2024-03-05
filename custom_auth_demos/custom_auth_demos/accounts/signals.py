from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from custom_auth_demos.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    create_profile(instance)
    # send_successful_registration_email(instance)


@receiver(post_save, sender=UserModel)
def send_successful_registration_email(user):
    pass


def create_profile(instance):
    if not created:
        return

    # profile = instance.profile

    if Profile.objects.filter(pk=instance.pk).first():
        return

    Profile.objects.create(user=instance)
