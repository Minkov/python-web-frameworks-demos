import time

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task
def slow_operation():
    print(f'Slow operation started at {time.time()}')
    time.sleep(2)
    print(f'Slow operation ended at {time.time()}')


# send_on_successful_registration_email()
@shared_task
def send_example_email(users_count, groups_count):
    # Simulate sending an email
    time.sleep(5)

    context = {
        "users_count": users_count,
        "groups_count": groups_count,
    }

    html_message = render_to_string("web/emails/example_email.html", context)
    message = strip_tags(html_message)

    send_mail(
        subject="Welcome to our site!",
        message=message,
        html_message=html_message,
        from_email="donchominkov@gmail.com",
        recipient_list=["doncho@ambitioned.com"],
    )


'''
# Web application:
- Initiate tasks (Schedule)

# Celery workers:
- Handle tasks

'''
