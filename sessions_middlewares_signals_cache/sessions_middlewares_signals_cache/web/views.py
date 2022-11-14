import random
from time import sleep

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views import generic as views

from sessions_middlewares_signals_cache.web.models import Employee

CLICKS_COUNT_SESSION_KEY = 'CLICKS_COUNT_SESSION_KEY'
LATEST_VALUES_SESSION_KEY = 'LATEST_VALUES_SESSION_KEY'

UserModel = get_user_model()


def very_slow_operation():
    sleep(10)
    return random.randint(1, 1024)


@cache_page(1 * 60)
def index(request):
    emp = Employee.objects.get(pk=5)

    Employee.objects.create(
        first_name='Doncho',
        last_name='Minkov',
        age=19,
    )
    value = very_slow_operation()

    latest_values = request.session.get(LATEST_VALUES_SESSION_KEY, [])
    latest_values = [value] + latest_values
    latest_values = latest_values[:3]
    request.session[LATEST_VALUES_SESSION_KEY] = latest_values

    return HttpResponse(f'Value: {value}; Latest values: {", ".join(str(x) for x in latest_values)}')


def show_session(request):
    clicks_count = request.session.get(CLICKS_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICKS_COUNT_SESSION_KEY] = clicks_count

    return HttpResponse(f'Clicks: {clicks_count}')


def raise_error(request):
    UserModel.objects.get(pk=100010)


class EmployeesListView(views.ListView):
    model = Employee
    template_name = 'employees/list.html'
    default_paginate_by = 3

    # paginate_by = 4

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.default_paginate_by)
