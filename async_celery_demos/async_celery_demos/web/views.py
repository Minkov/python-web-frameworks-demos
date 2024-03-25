import time

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render

from async_celery_demos.web.tasks import slow_operation, send_example_email

UserModel = get_user_model()


def get_user_count():
    print("Getting users count...")
    return UserModel.objects.count()


def get_groups_count():
    print("Getting groups count...")
    return Group.objects.count()


def index(request):
    users_count = get_user_count()
    groups_count = get_groups_count()

    title = "It works!"

    context = {
        "title": title,
        "users_count": users_count,
        "groups_count": groups_count,
    }

    send_example_email.delay(users_count, groups_count)

    # for _ in range(500):
    #     slow_operation.delay()
    #     # slow_operation()

    return HttpResponse(str(context))


'''
# Sync code

Servant 1:
1. Get coffee - 1 hour
2. Get milk - 1.5 hours
3. Prepare coffee with milk - 0.5 hours

Coffee with milk done in 3 hours

# Async code

Servant 1:                      | Servant 2:
1. Get coffee - 1 hours         | 1. Get milk - 1.5 hours

Servant 1 or 2:
1. Prepare coffee with milk - 0.5 hours

Coffee with milk done in 2 hours
'''
