from django.shortcuts import redirect
from django.utils import timezone


# `get_response` gets the response from **next middleware** or **view**
def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = timezone.now()

        response = get_response(request, *args, **kwargs)

        end_time = timezone.now()
        print(f'(func) Executed in {end_time - start_time}')

        return response

    return middleware


class MeasureTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        return self._middleware(*args, **kwargs)

    def _middleware(self, request, *args, **kwargs):
        start_time = timezone.now()

        response = self.get_response(request, *args, **kwargs)

        end_time = timezone.now()
        print(f'(class) Executed in: {end_time - start_time}')

        return response


def redirect_to_index_on_error_middleware(get_response):
    def middleware(*args, **kwargs):
        response = get_response(*args, **kwargs)

        if response.status_code == 500:
            return redirect('index')

        return response

    return middleware


def login_required_middleware(get_response):
    def middleware(request, *args, **kwargs):
        # check if this is the `login` page
        if not request.user.is_authenticated:
            return redirect('admin:login')

        return get_response(request, *args, **kwargs)

    return middleware
