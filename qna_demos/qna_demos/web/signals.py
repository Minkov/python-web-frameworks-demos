from django.contrib.auth.models import Group


def user_created(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get_or_create(name="Web Developer")
        instance.groups.add(group)
        instance.save()
