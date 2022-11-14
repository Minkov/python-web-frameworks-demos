from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from sessions_middlewares_signals_cache.web.models import Employee

UserModel = get_user_model()


@receiver(signals.post_save, sender=Employee)
def handle_employee_created(*args, **kwargs):
    print(args)
    print(kwargs)


@receiver(signals.post_save, sender=UserModel)
def create_employee_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return
    print(instance.pk)
    Employee.objects.create(
        user_id=instance.pk,
    )


@receiver(signals.post_save, sender=UserModel)
def send_register_email_on_create(instance, created, *args, **kwargs):
    if not created:
        return


'''
kwargs = {
    'signal': <django.db.models.signals.ModelSignal object at 0x7f4d867f9120>, 
    'sender': <class 'sessions_middlewares_signals_cache.web.models.Employee'>,
    'instance': <Employee: Employee object (1)>,
    'created': True, 
    'update_fields': None,
    'raw': False, 
    'using': 'default'
}
'''
